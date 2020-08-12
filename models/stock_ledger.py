from odoo import models, fields, api
from odoo.exceptions import UserError
import random
from odoo import http
import json
import datetime
# from odoo.tools.misc import formatLang



class StockLedger(models.Model):
    _name = 'stock.ledger'
    _description = 'this is stock ledger'
    name = fields.Char(string="报表名称")
    startDate = fields.Date(string="开始期间", required=True)
    endDate = fields.Date(string="结束期间", required=True)
    fast_period = fields.Date(string="选取期间")
    company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id',
                                          string="Company Currency", readonly=True, store=True)
    company_id = fields.Many2one('res.company', string='公司',
                                 store=True, index=True, readonly=True, required=True, default=lambda self:self.env.user.company_id.id)
    repositories = fields.Many2one('stock.location', string='仓库位置',
                                   store=True, index=True, readonly=False, required=True)
    customer = fields.Many2one('stock.location', string='客户位置',
                               default=lambda self:self.env['stock.location'].search([('usage', '=' ,'customer')],limit=1).id, required=True)
    supplier = fields.Many2one('stock.location', string='供应商位置',
                               default=lambda self: self.env['stock.location'].search([('usage', '=', 'supplier')],
                                                                                      limit=1).id, required=True)
    line_ids = fields.One2many('stock.ledger.line', 'move_id', string='库存总账明细',
                               copy=True, readonly=True, ondelete="Cascade")



    def open_stock(self):
        currency = self.env.user.company_id.currency_id
        startDate = self.startDate.isoformat()
        endDate = self.endDate.isoformat()
        company_id = self.company_id.id
        repositories = self.repositories.id
        customer = self.customer.id
        supplier = self.supplier.id
        sql = "SELECT sm.product_id, (select product_template.name as name from product_product, product_template WHERE product_product.id = sm.product_id AND product_product.product_tmpl_id = product_template.id limit 1), \
              (SUM ( CASE WHEN location_id = {0} AND location_dest_id = {1} THEN product_qty ELSE 0 END ) - SUM ( CASE WHEN location_id = {1} AND location_dest_id = {0} THEN product_qty ELSE 0 END )) AS out_mount, \
              (SUM ( CASE WHEN location_id = {0} AND location_dest_id = {1} THEN value ELSE 0 END ) * -1  - SUM ( CASE WHEN location_id = {1} AND location_dest_id = {0} THEN value ELSE 0 END )) AS out_value, \
              (SUM ( CASE WHEN location_id = {2} AND location_dest_id = {0} THEN product_qty ELSE 0 END ) - SUM ( CASE WHEN location_id = {0} AND location_dest_id = {2} THEN product_qty ELSE 0 END )) AS in_mount, \
              (SUM ( CASE WHEN location_id = {2} AND location_dest_id = {0} THEN value ELSE 0 END ) + SUM ( CASE WHEN location_id = {0} AND location_dest_id = {2} THEN value ELSE 0 END )) AS in_value \
              FROM stock_move as sm WHERE write_date >= '{3}' AND write_date <= '{4}' AND company_id = {5} AND state= 'done' GROUP BY sm.product_id".format(repositories, customer, supplier, startDate, endDate, company_id)

        self.env.cr.execute(sql)
        result = self.env.cr.dictfetchall()

        for line in result:
            move_id = self.id
            product_name = line.get('name')
            stock_in = line.get('in_mount')
            stock_in_value = line.get('in_value')
            stock_out = line.get('out_mount')
            stock_out_value = line.get('out_value')
            product_id = line.get('product_id')
            product = self.env['product.product'].search([('id', '=', product_id)], limit=1)
            categories = product.product_tmpl_id.categ_id.complete_name
            stock_in_hand = product.product_tmpl_id.qty_available
            uom = product.product_tmpl_id.uom_name
            uom_value = product.product_tmpl_id.standard_price
            qty_repositories = self.env['stock.location'].search([('id', '=', repositories)], limit=1)
            qty = self.env['stock.quant']._get_available_quantity(product, qty_repositories)
            qyt_value = uom_value * qty

            result = {
                'product_name' : product_name,
                'categories' : categories,
                'stock_in' : stock_in,
                'stock_in_value' : stock_in_value,
                'stock_out' : stock_out,
                'stock_out_value' : stock_out_value,
                'stock_in_hand' : stock_in_hand,
                'repositories_in_hand' : qty,
                'qyt_value' : qyt_value,
                'uom' : uom,
                'uom_value' : uom_value,
                'move_id': move_id,

            }
            self.env['stock.ledger.line'].create(result)



class StockLedgerLine(models.Model):
    _name = 'stock.ledger.line'
    _description = 'this is stock ledger line'
    product_name = fields.Char(string='产品名称')
    move_id = fields.Many2one('stock.ledger', string='库存总账', ondelete="Cascade", index=True,
                              auto_join=True)
    stock_in = fields.Float(default=0.0, string="入库数量",
                            store=True, digits=(10, 2), readonly=True)
    stock_in_value = fields.Float(default=0.0, string="入库成本",
                            store=True, digits=(10, 2), readonly=True)
    stock_out = fields.Float(default=0.0, string="出库数量",
                             store=True, digits=(10, 2), readonly=True)
    stock_out_value = fields.Float(default=0.0, string="出库成本",
                             store=True, digits=(10, 2), readonly=True)
    stock_in_hand = fields.Float(default=0.0, string="在手数量",
                                 store=True, digits=(10, 2), readonly=True)
    repositories_in_hand = fields.Float(default=0.0, string="仓库在手",
                                 store=True, digits=(10, 2), readonly=True)
    uom_value = fields.Float(default=0.0, string="单位成本",
                                        store=True, digits=(10, 2), readonly=True)
    qyt_value = fields.Float(default=0.0, string="库存金额",
                                        store=True, digits=(10, 2), readonly=True)
    uom = fields.Char(string='单位')
    categories = fields.Char(string='产品类别')

    @api.multi
    def create(self, vals):
        return super(StockLedgerLine, self).create(vals)










# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import datetime
from odoo.http import request

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # auroral 2020-5-25
    @api.multi
    @api.onchange('user_id')
    def onchange_user_id(self):
        self.team_id = self.user_id.sale_team_id
    # auroral 2020-5-25



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    discount_after_unit = fields.Monetary(string='折扣后单价', default=0.0, store=True, compute='_compute_discount_after_unit',
                                          readonly=True)
    discount_after_margin = fields.Monetary(string='折扣后毛利', default=0.0, store=True,
                                          compute='_compute_discount_after_margin',
                                          readonly=True)


    @api.depends('discount', 'price_unit')
    def _compute_discount_after_unit(self):
        for line in self:
            discount_after_unit = line.price_unit * ((100 - line.discount or 0.0) / 100.0)
            line.update({
                'discount_after_unit' : discount_after_unit
            })

    @api.depends('product_uom_qty', 'price_subtotal', 'purchase_price')
    def _compute_discount_after_margin(self):
        for line in self:
            discount_after_margin = line.price_subtotal - (line.product_uom_qty * line.purchase_price)
            line.update({
                'discount_after_margin' : discount_after_margin
            })
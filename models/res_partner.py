# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pricelist_id = fields.Many2one('product.pricelist', string=u'指定价格表')


class ResWebsite(models.Model):
    _inherit = 'website'

    def get_pricelist_available(self, show_visible=False):
        user_partner_id = self.env.user.partner_id.id
        pricelists_id = self.env['res.partner'].browse(user_partner_id).pricelist_id.id
        return self.env['product.pricelist'].browse(pricelists_id)
        # auroral 2020-5-25
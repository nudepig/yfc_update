# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # auroral 2020-5-25
    @api.multi
    @api.onchange('user_id')
    def onchange_user_id(self):
        self.team_id = self.user_id.sale_team_id
    # auroral 2020-5-25
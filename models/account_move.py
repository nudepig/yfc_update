# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    team_id = fields.Many2one('crm.team', '销售团队', change_default=True)


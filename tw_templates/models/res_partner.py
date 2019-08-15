# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.partner'

    account_bank =fields.Char("Tài khoản ngân hàng")

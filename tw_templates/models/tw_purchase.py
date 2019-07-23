# -*- coding: utf-8 -*-

from odoo import fields, models, api


class PurchaseOder(models.Model):
    _inherit = 'purchase.order'

    person_set = fields.Many2one('res.users',string="Người đặt hàng")
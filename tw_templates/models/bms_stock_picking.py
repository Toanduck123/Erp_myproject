# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Stockpicking(models.Model):
    _inherit = 'stock.picking'
    person = fields.Many2one('res.partner',string="Người nhận hàng")
    payment = fields.Char("Payment: ")

    @api.model
    def create(self, values):
        record = super(Stockpicking, self).create(values)
        print(values)

        return record
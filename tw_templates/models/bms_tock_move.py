# -*- coding: utf-8 -*-

from odoo import fields, models, api


class StockpickingMove(models.Model):
    _inherit = 'stock.move'

    vat_ids = fields.Many2many('account.tax')
    price_vat = fields.Float('giá sau thuế')
    total = fields.Float("Tổng giá")

    @api.model
    def create(self, values):
        print(values)
        if 'sale_line_id' in values:
            sale_order_line = self.env['sale.order.line'].search([('id', '=', values['sale_line_id'])]).tax_id
            if sale_order_line:
                product = self.env['product.template'].search([('id','=',values['product_id'])]).lst_price
                vat_ids = sale_order_line
                price_vat = (sale_order_line.amount / 100 + 1) * product
                total = ((sale_order_line.amount / 100 + 1) * product) * values['product_uom_qty']
                values['vat_ids'] = [(6,0,[vat_ids.id])]
                values['price_vat'] = price_vat
                values['total'] = total
        return super(StockpickingMove, self).create(values)
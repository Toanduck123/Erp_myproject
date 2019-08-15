# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": 'BMS Template Improvement',
    "summary": 'BMS',
    "version": "10.0.0.1",
    "category": "BMSAPP",
    "website": "",
    "author": "BMSTECH",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "depends": ['base', 'product', 'hr', 'sale', 'mail', 'purchase', 'stock'],
    "data": [
        'report/template_sale_order.xml',
        'report/template_email.xml',
        'report/content_sale_order.xml',
        'report/content_invoice.xml',
        'report/template_purchase.xml',
        'report/template_purchase_quotation.xml',
        'report/tw_purchase.xml',

        'report/packing_list.xml',
        'report/tw_stock_picking.xml',
        'report/tw_views_picking.xml',
        'report/tw_company.xml',
        # 'views/res_partner.xml',
    ],
    'qweb': [],
}

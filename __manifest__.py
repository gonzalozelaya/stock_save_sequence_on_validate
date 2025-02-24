# -*- coding: utf-8 -*-
{
    'name': "Add route to sale order",

    'summary': """
        Allows to pick route on sale order""",

    'description': """
         Allows to pick route on sale order
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_stock','sale'],
    'data':[
        'views/sale_order_views.xml'
    ]
}
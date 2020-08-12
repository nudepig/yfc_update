# -*- coding: utf-8 -*-
{
    'name': "yfc_update",

    'summary': """
        继承的方式重写一些模型方法和视图""",

    'description': """
        1.针对不同的网站用户，展示不同的价格表，用户价格表首先在联系人中配置指定的价格表
        2.销售订单中的其他信息销售员绑定销售团队
    """,

    'author': "auroral",
    'website': "https://erp.yunfc.net/",
    'images': ['static/description/icon.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'yfc',
    'version': '0.2',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_sale','account','purchase','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/stock_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order.xml',
        'views/account_view.xml',
        'views/purchase_view.xml',
        'views/stock_ledger.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
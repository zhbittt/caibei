{
    'name': 'Access Record',
    'description': '客户访问记录',
    'author': 'caibei',
    'depends': [
        'base',
    ],
    'application': True,
    'data': [
        'security/access_record_security.xml',
        'security/ir.model.access.csv',
        'views/access_record_menu.xml',
        'views/access_record_views.xml',
        'views/crm_sale_customer_views.xml',
    ]
}

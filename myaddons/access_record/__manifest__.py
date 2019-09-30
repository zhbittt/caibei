{
    'name': 'Access Record',
    'description': '客户访问记录',
    'author': 'caibei',
    'depends': [
        'base',
        'crm'
    ],
    'application': False,
    'data': [
        'security/access_record_security.xml',
        'security/ir.model.access.csv',
        'views/access_record_views.xml',
        'views/customer_views.xml',
    ]
}

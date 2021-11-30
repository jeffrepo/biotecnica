# -*- coding: utf-8 -*-


{
    'name': 'Biotecnica',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Desarrollos para Biotecnica',
    'description': """

""",
    'depends': ['sale','account'],
    'data': [
        'views/sale_views.xml',
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}

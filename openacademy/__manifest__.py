# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage Academy""",

    'description': """
    Open Academy module for managing trainings:
    -training courses
    -training sessions
    -attendees registration
    """,

    'author': "Roman",
    'website': "http://www.roman.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
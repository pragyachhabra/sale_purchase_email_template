# -*- coding: utf-8 -*-
{
    'name': "mail_template",
    "version": "1.0",
    "author": "Linserv AB",

    'summary': """
        A demo module that shows you how to create your own e-mail templates""",

    'description': """
        A demo module that shows you how to create your own e-mail templates
    """,

        "website": "www.linserv.se",
    "contributors": [
        'Pragya Chhabra <pragyachhabbra@gmail.com>'
    ],
    "license": "",


    # any module necessary for this one to work correctly
    'depends': ['mail','contacts'],

    # always loaded
    'data': [
        'views/mail_template.xml',
        'views/sale_report.xml',
        'views/purchase_report.xml',
    ],

    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}
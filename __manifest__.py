# -*- coding: utf-8 -*-
{
    'name': "Siswa",

    'summary': """
        Aplikasi Database Siswa""",

    'description': """
        Aplikasi Database Siswa
        Untuk Sekolah PG/TK/RA
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/tahunajaran.xml',
        'views/rombel.xml',
        'views/pekerjaan.xml',
        'views/siswa.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
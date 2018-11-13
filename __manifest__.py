# -*- coding: utf-8 -*-
{
    'name': "Base Siswa",

    'summary': """
        Aplikasi Database Siswa""",

    'description': """
        Aplikasi Database Siswa
        Untuk Sekolah PG/TK/RA
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_model_data.xml',
        'views/tahunajaran.xml',
        'views/jenjang.xml',
        'views/rombel.xml',
        'views/pekerjaan.xml',
        # 'views/siswa.xml',
        'views/res_siswa.xml',
        'views/guru.xml',
        'views/rombel_siswa.xml',
        'views/rombel_dashboard.xml',
        # 'views/siswa_dashboard_view.xml',
        'views/wizard_pindah_kelas.xml',
        # 'views/wizard_mutasi.xml',
        'views/wizard_non_aktif.xml',
        'views/wizard_report_rekap_siswa.xml',
        'views/wizard_report_form_presensi.xml',
        # 'views/wizard_naik_kelas.xml',
        'report/report_master.xml',
        'report/report_siswa.xml',
        'report/report_rekap_siswa.xml',
        'report/report_form_presensi.xml',
        'views/menu.xml',
        'data/ir_default_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
} 
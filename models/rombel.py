# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rombel(models.Model):
    _name = 'siswa_ocb11.rombel'

    name = fields.Char(string="Nama", required=True)
    # jenjang = fields.Selection([(1, 'PG'), (2, 'TK A'), (3, 'TK B')], string='Jenjang', required=True, default=1)
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang',string='Jenjang', required=True)
    siswas = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='rombel_id' , string='Siswa')
    kapasitas = fields.Integer('Kapasitas', required=True, default=0)

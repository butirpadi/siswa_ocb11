# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rombel(models.Model):
    _name = 'siswa_ocb11.rombel'

    name = fields.Char(string="Nama", required=True)
    jenjang = fields.Selection([('0', 'Play Group'), ('1', 'TK A'), ('2', 'TK B')], string='Jenjang', required=True, default='none')
    siswas = fields.One2many('siswa_ocb11.rombel_siswa',inverse_name='rombel_id' ,string='Siswa')
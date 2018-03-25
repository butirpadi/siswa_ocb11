# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rombel_siswa(models.Model):
    _name = 'siswa_ocb11.rombel_siswa'

    siswa_id = fields.Many2one('siswa_ocb11.siswa', string='Siswa')
    rombel_id = fields.Many2one('siswa_ocb11.rombel', string="Rombongan Belajar")
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran')
    
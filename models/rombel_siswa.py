# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rombel_siswa(models.Model):
    _name = 'siswa_ocb11.rombel_siswa'

    siswa_id = fields.Many2one('res.partner', string='Siswa', ondelete='restrict')
    rombel_id = fields.Many2one('siswa_ocb11.rombel', string="Rombongan Belajar")
    jenjang = fields.Selection([(1, 'PG'), (2, 'TK A'), (3, 'TK B')], string='Jenjang', related='rombel_id.jenjang')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran')
    # related field to siswa
    induk = fields.Char(related='siswa_id.induk', string='Induk')
    nis = fields.Char(related='siswa_id.nis', string='NIS')
    panggilan = fields.Char(related='siswa_id.panggilan', string='Panggilan')
    jenis_kelamin = fields.Selection([('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin', related='siswa_id.jenis_kelamin')
    
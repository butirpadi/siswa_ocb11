# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint
import calendar

class tahunajaran_jenjang(models.Model):
    _name = 'siswa_ocb11.tahunajaran_jenjang'

    name = fields.Char(string='Nama')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', required=True, ondelete='cascade')
    # jenjang = fields.Selection([(1, 'PG'), (2, 'TK A'), (3, 'TK B')], string='Jenjang', required=True, default=1)
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang',string='Jenjang', required=True, ondelete='cascade')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('valid', 'Validated'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

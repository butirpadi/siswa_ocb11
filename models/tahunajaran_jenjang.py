# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint
import calendar

class tahunajaran_jenjang(models.Model):
    _name = 'siswa_ocb11.tahunajaran_jenjang'

    name = fields.Char(string='Nama')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', required=True, ondelete='cascade')
    jenjang = fields.Selection([(0, 'PG'), (1, 'TK A'), (2, 'TK B')], string='Jenjang', required=True, default=0)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('valid', 'Validated'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

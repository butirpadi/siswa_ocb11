# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from pprint import pprint

class guru(models.Model):
    _name = 'siswa_ocb11.guru'

    active = fields.Boolean(default=True)
    nik = fields.Char(string="NIK", required=True)
    name = fields.Char(string="Nama", required=True)
    panggilan = fields.Char(string="Panggilan")
    jenis_kelamin = fields.Selection([('laki', 'Pria'), ('perempuan', 'Wanita')], string='Jenis Kelamin', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir',required=True)
    tempat_lahir = fields.Char(string='Tempat Lahir', required=True)
    alamat = fields.Char(string='Alamat')
    telp = fields.Char(string='Telp')
     
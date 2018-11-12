# -*- coding: utf-8 -*-

from flectra import models, fields, api

class pekerjaan(models.Model):
    _name = 'siswa_ocb11.pekerjaan'

    name = fields.Char(string="Nama", required=True)
     
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jenjang(models.Model):
    _name = 'siswa_ocb11.jenjang'

    name = fields.Char(string="Nama", required=True)

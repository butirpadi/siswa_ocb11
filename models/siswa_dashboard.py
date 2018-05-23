# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SiswaDashboard(models.Model):
    _name = 'siswa_ocb11.siswa_dashboard'

    def _get_jumlah_siswa(self):
        return 10


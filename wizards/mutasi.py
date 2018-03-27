from odoo import models, fields, api
from pprint import pprint

class mutasi(models.TransientModel):
    _name = 'siswa_ocb11.mutasi'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)], required=True)
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True)
    mutasi_ke = fields.Char(string='Mutasi ke')
    keterangan = fields.Char(string='Keterangan')
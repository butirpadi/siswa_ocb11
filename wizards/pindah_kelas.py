from odoo import models, fields, api
from pprint import pprint

class pindah_kelas(models.TransientModel):
    _name = 'siswa_ocb11.pindah_kelas'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)])
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]))
    # tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    rombel_asal_id = fields.Many2one('siswa_ocb11.rombel', string="Rombel" , compute='_compute_rombel_asal')
    rombel_tujuan_id = fields.Many2one('siswa_ocb11.rombel', string="Pindah ke" )

    @api.depends('siswa_id')
    def _compute_rombel_asal(self):
        if self.siswa_id:
            for rec in self:
                # ta_aktif = self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)])
                tahunajaran = rec.tahunajaran_id
                # print(tahunajaran.name)
                # print(rec.siswa_id.name)
                # print(rec.siswa_id.id)
                rombel_asal = rec.siswa_id.rombels.search([('siswa_id','=',rec.siswa_id.id),('tahunajaran_id','=',tahunajaran.id)])
                pprint(rec.siswa_id.rombels)
                rec.rombel_asal_id = rec.siswa_id.active_rombel_id.id
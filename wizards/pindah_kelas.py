from odoo import models, fields, api
from pprint import pprint

class pindah_kelas(models.TransientModel):
    _name = 'siswa_ocb11.pindah_kelas'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)], required=True)
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True)
    # tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    rombel_asal_id = fields.Many2one('siswa_ocb11.rombel', string="Rombel" , compute='_compute_rombel_asal', required=True)
    rombel_tujuan_id = fields.Many2one('siswa_ocb11.rombel', string="Pindah ke", required=True)

    @api.depends('siswa_id')
    def _compute_rombel_asal(self):
        if self.siswa_id:
            for rec in self:
                # set rombel asal
                tahunajaran = rec.tahunajaran_id
                rombel_asal = rec.siswa_id.rombels.search([('siswa_id','=',rec.siswa_id.id),('tahunajaran_id','=',tahunajaran.id)])
                rec.rombel_asal_id = rec.siswa_id.active_rombel_id.id
                # filter rombel tujuan
                print('Jenjang : ' + str(rec.rombel_asal_id.jenjang))
    
    @api.model
    def create(self, vals):
        # print(vals['siswa_id'])
        # print(vals['tahunajaran_id'])
        # # print(self.rombel_asal_id)
        # print(vals['rombel_tujuan_id'])
        # pprint(vals)

        # rombel_asal = self.env['siswa_ocb11.rombel_siswa'].search([('siswa_id','=',vals['siswa_id']),('tahunajaran_id','=',vals['tahunajaran_id'])])
        # print(rombel_asal.id)

        # update rombel
        self.env['siswa_ocb11.rombel_siswa'].search([('siswa_id','=',vals['siswa_id']),('tahunajaran_id','=',vals['tahunajaran_id'])]).write({
            'rombel_id' : vals['rombel_tujuan_id']
        })
        siswa = self.env['res.partner'].search([('id','=',vals['siswa_id'])])
        print('recompute rombel siswa')
        siswa._compute_rombel()

        result = super(pindah_kelas, self).create(vals)
        
        return result
from flectra import models, fields, api, _
from pprint import pprint
from datetime import datetime

class wizard_report_rekap_siswa(models.TransientModel):
    _name = 'siswa_ocb11.wizard_report_rekap_siswa'

    name = fields.Char('Name', default='Report Kas')
    rombel_id = fields.Many2one('siswa_ocb11.rombel', required=True, string='Rombongan Belajar', ondelete="cascade")
    siswa_ids = fields.Many2many('res.partner',relation='siswa_ocb11_report_siswa_rel', column1='report_id',column2='siswa_id', string="Data Siswa", ondelete="cascade")
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True, ondelete="cascade")
    
    def action_save(self):
        self.ensure_one()
        # set kas_ids
        # siswas = self.env['res.partner'].search([('active_rombel_id','=',self.rombel_id.id)])
        siswas = self.env['siswa_ocb11.rombel_siswa'].search([('tahunajaran_id','=',self.tahunajaran_id.id),('rombel_id','=',self.rombel_id.id)])
        # reg_sis = []
        for sis in siswas:
            self.write({
                'siswa_ids' : [(4,sis.siswa_id.id)]
            })
        return self.env.ref('siswa_ocb11.report_rekap_siswa_action').report_action(self)
        
        


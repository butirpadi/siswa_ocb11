from odoo import models, fields, api
from pprint import pprint

class pindah_kelas(models.TransientModel):
    _name = 'siswa_ocb11.pindah_kelas'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)], required=True)
    induk = fields.Char('Induk',related='siswa_id.induk')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True)
    # tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    rombel_asal_id = fields.Many2one('siswa_ocb11.rombel', string="Rombel" , compute='_compute_rombel_asal', store=True)
    # rombel_tujuan_id = fields.Many2one('siswa_ocb11.rombel', string="Pindah ke", required=True, domain=lambda self: [('jenjang_id', '=', self.rombel_asal_id.jenjang_id.id)])
    rombel_tujuan_id = fields.Many2one('siswa_ocb11.rombel', string="Pindah ke", required=True, )

    @api.depends('siswa_id')
    def _compute_rombel_asal(self):
        # if self.siswa_id:
        for rec in self:
            if rec.siswa_id:
                # set rombel asal
                tahunajaran = rec.tahunajaran_id
                rombel_asal = rec.siswa_id.rombels.search([('siswa_id','=',rec.siswa_id.id),('tahunajaran_id','=',tahunajaran.id)])
                rec.rombel_asal_id = rec.siswa_id.active_rombel_id.id
    
    @api.onchange('rombel_asal_id')
    def rombel_asal_change(self):
        if self.rombel_asal_id:
            domain = {'rombel_tujuan_id':[
                            ('jenjang_id','=',self.rombel_asal_id.jenjang_id.id),
                            ('id','!=',self.rombel_asal_id.id)
                        ]}
            return {'domain':domain, 'value':{'rombel_tujuan_id':[]}}
    
    def action_pindah_kelas(self):
        # update rombel
        self.env['siswa_ocb11.rombel_siswa'].search([
            ('siswa_id','=',self.siswa_id.id),
            ('tahunajaran_id','=',self.tahunajaran_id.id)
            ]).write({
                    'rombel_id' : self.rombel_tujuan_id.id
                })
        siswa = self.env['res.partner'].search([('id','=',self.siswa_id.id)])
        print('recompute rombel siswa')
        siswa._compute_rombel()

        # update rombel siswa dashboard
        rombel_dashboards = self.env['siswa_ocb11.rombel_dashboard'].search([
                    ('tahunajaran_id', '=', self.tahunajaran_id.id),
                    ('rombel_id', 'in', [self.rombel_tujuan_id.id, self.rombel_asal_id.id])
                ])

        # pprint(rombel_dashboards)
        for rbd in rombel_dashboards:
            print('loop rombel dashboard')
            rbd.lets_compute_jumlah_siswa()
        
        # reload page
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

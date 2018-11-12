from flectra import models, fields, api
from pprint import pprint
from datetime import datetime

class non_aktif(models.TransientModel):
    _name = 'siswa_ocb11.non_aktif'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)], required=True)
    induk = fields.Char('Induk',related='siswa_id.induk')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True)
    rombel_asal_id = fields.Many2one('siswa_ocb11.rombel', string="Rombel" , compute='_compute_rombel_asal')
    # non_aktif_selection = fields.Selection([('mutasi', 'Mutasi'), ('lulus', 'Lulus'), ('meninggal', 'Meninggal Dunia')], string='Sebab', required=True)
    non_aktif_selection = fields.Selection([('mutasi', 'Mutasi'), ('meninggal', 'Meninggal Dunia')], string='Sebab', required=True)
    keterangan = fields.Char('Keterangan')
    tanggal  = fields.Date('Tanggal', required=True, default=datetime.today())

    @api.depends('siswa_id')
    def _compute_rombel_asal(self):
        if self.siswa_id:
            for rec in self:
                # set rombel asal
                tahunajaran = rec.tahunajaran_id
                rombel_asal = rec.siswa_id.rombels.search([('siswa_id','=',rec.siswa_id.id),('tahunajaran_id','=',tahunajaran.id)])
                rec.rombel_asal_id = rec.siswa_id.active_rombel_id.id
    
    # @api.model
    # def create(self, vals):
    #     result = super(non_aktif, self).create(vals)
    #     # update status siswa        
    #     self.env['res.partner'].search([('id','=',result.siswa_id.id)]).write({
    #         'active' : False,
    #         'non_aktif_selection' : result.non_aktif_selection,
    #         'tanggal_non_aktif' : result.tanggal
    #     })
        
    #     return result
    
    @api.multi
    def action_save(self):
        self.env['res.partner'].search([('id','=',self.siswa_id.id)]).write({
            'active' : False,
            'non_aktif_selection' : self.non_aktif_selection,
            'tanggal_non_aktif' : self.tanggal,
            'tahunajaran_non_aktif_id' : self.tahunajaran_id.id
        })

        # set non active data di rombel_siswa
        self.env['siswa_ocb11.rombel_siswa'].search([
                ('siswa_id', '=', self.siswa_id.id),
                ('tahunajaran_id', '=', self.tahunajaran_id.id),
            ]).write({
                'active' : False
            })

        # tampilkan form non aktif
        return {
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'name': 'Siswa Non Aktif',
            'view_mode': 'tree, form',
            'res_model': 'res.partner',
            'target': 'current',
            'domain' : [('active','=',False),('is_siswa','=',True)],
            'context' : {'group_by': ['non_aktif_selection']},
        } 
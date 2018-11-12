from flectra import models, fields, api
from pprint import pprint

class mutasi(models.TransientModel):
    _name = 'siswa_ocb11.mutasi'

    siswa_id = fields.Many2one('res.partner', string="Siswa", domain=[('is_siswa','=',True)], required=True)
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)]), required=True)
    mutasi_ke = fields.Char(string='Mutasi ke')
    keterangan = fields.Char(string='Keterangan')
    rombel_asal_id = fields.Many2one('siswa_ocb11.rombel', string="Rombel" , compute='_compute_rombel_asal', required=True)

    @api.depends('siswa_id')
    def _compute_rombel_asal(self):
        if self.siswa_id:
            for rec in self:
                # set rombel asal
                tahunajaran = rec.tahunajaran_id
                rombel_asal = rec.siswa_id.rombels.search([('siswa_id','=',rec.siswa_id.id),('tahunajaran_id','=',tahunajaran.id)])
                rec.rombel_asal_id = rec.siswa_id.active_rombel_id.id
    
    @api.model
    def create(self, vals):
        result = super(mutasi, self).create(vals)
        # update status siswa        
        self.env['res.partner'].search([('id','=',result.siswa_id.id)]).write({
            'active' : False,
            'non_aktif_selection' : 'mutasi'
        })
        
        return result
     
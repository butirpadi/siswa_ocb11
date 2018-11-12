# -*- coding: utf-8 -*-

from flectra import models, fields, api, exceptions 
from pprint import pprint

class rombel_dashboard(models.Model):
    _name = 'siswa_ocb11.rombel_dashboard'

    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', ondelete="cascade")
    rombel_id = fields.Many2one('siswa_ocb11.rombel', string='Rombel', ondelete="cascade")
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang', related="rombel_id.jenjang_id")
    siswa_ids = fields.One2many('siswa_ocb11.rombel_siswa', related='rombel_id.siswas')
    jumlah_siswa = fields.Integer('Jumlah Siswa', compute="_compute_jumlah_siswa", store=True)    
    jumlah_laki = fields.Integer('Jumlah Laki-laki', compute="_compute_jumlah_siswa", store=True)    
    jumlah_perempuan = fields.Integer('Jumlah Perempuan', compute="_compute_jumlah_siswa", store=True)   
    color = fields.Integer(string='Color Index') 

    def get_view_rombel(self):
        return {
                'name': 'Data Siswa ' + self.rombel_id.name + ' ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'tree',
                'res_model': 'siswa_ocb11.rombel_siswa',
                'target': 'current',
                'domain' : [('tahunajaran_id', '=', self.tahunajaran_id.id), ('rombel_id', '=', self.rombel_id.id)],
                'type': 'ir.actions.act_window',
            }
    
    def get_view_rombel_laki(self):
        return self.get_view_rombel_by_jk('laki')
    
    def get_view_rombel_perempuan(self):
        return self.get_view_rombel_by_jk('perempuan')
    
    def get_view_rombel_by_jk(self, jKel):
        return {
                'name': 'Data Siswa ' + self.rombel_id.name + ' ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'tree',
                'res_model': 'siswa_ocb11.rombel_siswa',
                'target': 'current',
                'domain' : ['&','&',('tahunajaran_id', '=', self.tahunajaran_id.id), 
                            ('rombel_id', '=', self.rombel_id.id),
                            ('jenis_kelamin', '=', jKel)
                            ],
                'type': 'ir.actions.act_window',
            }

    @api.depends('rombel_id')
    def _compute_jumlah_siswa(self):
        self.lets_compute_jumlah_siswa()
    
    def lets_compute_jumlah_siswa(self):
        print('inside lets compute jumlah siswa')
        for rec in self:
            # get jumlah siswa
            data_siswa = rec.siswa_ids.filtered(lambda r: r.tahunajaran_id.id == rec.tahunajaran_id.id)
            data_siswa = data_siswa.filtered(lambda r: r.rombel_id.id == rec.rombel_id.id)
            rec.jumlah_siswa = len(data_siswa)
            print('Jumlah Siswa : ' + str(len(data_siswa)))

            #get jumlah siswa laki-laki
            data_siswa_laki = data_siswa.filtered(lambda r: r.siswa_id.jenis_kelamin == 'laki')
            rec.jumlah_laki = len(data_siswa_laki)
            print('Jumlah Siswa Laki2 : ' + str(len(data_siswa_laki)))

            #get jumlah siswa perempuan
            data_siswa_perempuan = data_siswa.filtered(lambda r: r.siswa_id.jenis_kelamin == 'perempuan')
            rec.jumlah_perempuan = len(data_siswa_perempuan)
            print('Jumlah Siswa Perempuan : ' + str(len(data_siswa_perempuan))) 
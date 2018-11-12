# -*- coding: utf-8 -*-

from flectra import models, fields, api

class rombel_siswa(models.Model):
    _name = 'siswa_ocb11.rombel_siswa'

    name = fields.Char('Name', related='siswa_id.name')
    active = fields.Boolean('Active', default=True)
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran')
    siswa_id = fields.Many2one('res.partner', string='Siswa', ondelete='restrict')
    rombel_id = fields.Many2one('siswa_ocb11.rombel', string="Rombongan Belajar")
    # jenjang = fields.Selection([(1, 'PG'), (2, 'TK A'), (3, 'TK B')], string='Jenjang', related='rombel_id.jenjang')
    # related field to siswa
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang',string='Jenjang', related='rombel_id.jenjang_id')
    induk = fields.Char(related='siswa_id.induk', string='Induk')
    nis = fields.Char(related='siswa_id.nis', string='NIS')
    panggilan = fields.Char(related='siswa_id.panggilan', string='Panggilan')
    jenis_kelamin = fields.Selection([('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin', related='siswa_id.jenis_kelamin', store=True)
    ayah = fields.Char(related='siswa_id.ayah', string='Nama Ayah')
    telp_ayah = fields.Char(related='siswa_id.telp_ayah', string='Telp Ayah')
    ibu = fields.Char(related='siswa_id.ibu', string='Nama Ibu')
    telp_ibu = fields.Char(related='siswa_id.telp_ibu', string='Telp Ibu')    

    @api.model
    def create(self, vals):
        result = super(rombel_siswa, self).create(vals)
        
        # update Rombel Dashboard
        print('Compute Rombel Siswa on Create')
        rb_dash = self.env['siswa_ocb11.rombel_dashboard'].search([
                        ('rombel_id','=',result.rombel_id.id),
                        ('tahunajaran_id','=',result.tahunajaran_id.id)
                    ])
        for dash in rb_dash:
            print('Loop for compute rombel siswa on create')
            dash.lets_compute_jumlah_siswa()

        return result
    
    @api.multi
    def unlink(self):
        tahunajaran_id  = 0
        rombel_id = 0
        
        # Update Rombel Dashboard
        for rec in self:
            print('Compute Rombel Siswa on Delete')
            tahunajaran_id = rec.tahunajaran_id.id
            rombel_id = rec.rombel_id.id
            # rb_dash = self.env['siswa_ocb11.rombel_dashboard'].search([
            #             ('rombel_id','=',rec.rombel_id.id),
            #             ('tahunajaran_id','=',rec.tahunajaran_id.id)
            #         ])
            # for dash in rb_dash:
            #     print('Loop for compute rombel siswa on delete')
            #     dash.lets_compute_jumlah_siswa()

        res =  super(rombel_siswa, self).unlink()

        # Update Rombel Dashboard
        rb_dash = self.env['siswa_ocb11.rombel_dashboard'].search([
                        ('rombel_id','=',rombel_id),
                        ('tahunajaran_id','=',tahunajaran_id)
                    ])
        for dash in rb_dash:
            print('Loop for compute rombel siswa on delete')
            dash.lets_compute_jumlah_siswa()

        return res

    # @api.multi
    # def write(self, vals):        
    #     # pprint(vals)
    #     # if 'rombels' in vals:
    #     #     # update jumlah siswa di rombel tersebut
    #     #     # get rombel id
    #     #     vals['rombels']

    #     print('adding/deleting rombel_siswa')
            
    #     result = super(rombel_siswa, self).write(vals)
    #     return result 
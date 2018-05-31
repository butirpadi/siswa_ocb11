# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions 
from pprint import pprint

class rombel(models.Model):
    _name = 'siswa_ocb11.rombel'

    name = fields.Char(string="Nama", required=True)
    # jenjang = fields.Selection([(1, 'PG'), (2, 'TK A'), (3, 'TK B')], string='Jenjang', required=True, default=1)
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang',string='Jenjang', required=True)
    siswas = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='rombel_id' , string='Siswa')
    kapasitas = fields.Integer('Kapasitas', required=True, default=0)

    color = fields.Integer(string='Color Index')
    is_show_on_dashboard = fields.Boolean('Show on Dashboard', default=False)

    @api.one
    def get_jumlah_siswa(self):        
        tahunajaran = self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)])
        
        print('tahunajaran : ' + str(tahunajaran.name))
        data_siswa = self.siswas.filtered(lambda r: r.tahunajaran_id.id == tahunajaran.id)
        return len(data_siswa)
    
    # @api.onchange('is_show_on_dashboard')
    # def show_on_dashboard_change(self):
    #     active_id = self._origin.id
        
    #     if self.is_show_on_dashboard:
    #         # insert to rombel_dashboard
    #         tahunajaran = self.env['siswa_ocb11.tahunajaran'].search([('name','ilike','%'),('active','ilike','%')])
    #         for ta in tahunajaran:
    #             print('create rombel_dasboard for tahunajaran : ' + ta.name + ' and rombel : '  + self.name)
    #             self.env['siswa_ocb11.rombel_dashboard'].create({
    #                 'rombel_id' : active_id,
    #                 'tahunajaran_id' : ta.id,
    #             })
    #     else:
    #         # self.env['siswa_ocb11.rombel_dashboard'].search([('rombel_id', '=', active_id)]).unlink()
    #         query = "delete from siswa_ocb11_rombel_dashboard where rombel_id =" + str(active_id)
    #         self.env.cr.execute(query)
    #         print('Rombel Dashboard Deleted')

    @api.multi
    def write(self, vals):
        if 'is_show_on_dashboard' in vals:
            active_id = self.id

            if vals['is_show_on_dashboard']:
                # insert to rombel_dashboard
                tahunajaran = self.env['siswa_ocb11.tahunajaran'].search([('name','ilike','%'),('active','ilike','%')])
                for ta in tahunajaran:
                    print('create rombel_dasboard for tahunajaran : ' + ta.name + ' and rombel : '  + self.name)
                    rb_dash = self.env['siswa_ocb11.rombel_dashboard'].create({
                    'rombel_id' : active_id,
                    'tahunajaran_id' : ta.id,
                    })
                    rb_dash.lets_compute_jumlah_siswa()
            else:
                # self.env['siswa_ocb11.rombel_dashboard'].search([('rombel_id', '=', active_id)]).unlink()
                query = "delete from siswa_ocb11_rombel_dashboard where rombel_id =" + str(active_id)
                self.env.cr.execute(query)
                print('Rombel Dashboard Deleted')
        
        result = super(rombel, self).write(vals)
        return result
            



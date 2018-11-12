# -*- coding: utf-8 -*-

from flectra import models, fields, api
from pprint import pprint

class jenjang(models.Model):
    _name = 'siswa_ocb11.jenjang'

    name = fields.Char(string="Nama", required=True)
    order = fields.Integer('Order')
    desc = fields.Char(string="Keterangan")
    
    @api.model
    def create(self, vals):        
        result = super(jenjang, self).create(vals)
        
        print('--------------------------------------------------------------------------')
        print('Auto generating tahunajaran jenjang for jenjang : ' + result.name)
        print('--------------------------------------------------------------------------')
        # auto generate biaya_registrasi on jenjang create
        tahunajaran_ids = self.env['siswa_ocb11.tahunajaran'].search([('id', 'ilike', '%'),('active', 'ilike', '%')])
        pprint(tahunajaran_ids)
        for ta in tahunajaran_ids:
            # get biaya_registrasi with jenjang
            tahunajaran_jenjang_ids = self.env['siswa_ocb11.tahunajaran_jenjang'].search([('tahunajaran_id', '=', ta.id),
                                                                                          ('jenjang_id', '=', result.id)])
            
            if not tahunajaran_jenjang_ids:
                self.env['siswa_ocb11.tahunajaran_jenjang'].create({
                    'name' : ta.name + ' ' + result.name,
                    'tahunajaran_id' : ta.id,
                    'jenjang_id' : result.id
                })
        
        return result    

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint

class siswa(models.Model):
    _inherit = 'res.partner'

    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Diterima', required=False)
    induk = fields.Char(string='Internal Reference', required=False, copy=False, readonly=True)
    nis = fields.Char(string="NIS", required=False)
    panggilan = fields.Char(string="Panggilan")
    jenis_kelamin = fields.Selection([('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin', required=False)
    tanggal_lahir = fields.Date(string='Tanggal Lahir',required=False)
    tempat_lahir = fields.Char(string='Tempat Lahir', required=False)
    alamat = fields.Char(string='Alamat')
    telp = fields.Char(string='Telp')
    ayah = fields.Char(string='Ayah')
    pekerjaan_ayah_id = fields.Many2one('siswa_ocb11.pekerjaan', string='Pekerjaan Ayah')
    telp_ayah = fields.Char(string='Telp. Ayah')
    ibu = fields.Char(string='Ibu')
    pekerjaan_ibu_id = fields.Many2one('siswa_ocb11.pekerjaan', string='Pekerjaan Ibu')
    telp_ibu = fields.Char(string='Telp. Ibu')
    rombels = fields.One2many('siswa_ocb11.rombel_siswa',inverse_name='siswa_id' ,string='Detail Rombongan Belajar')
    active_rombel_id = fields.Many2one('siswa_ocb11.rombel', string='Rombongan Belajar', compute='_compute_rombel', store=True)
    is_siswa = fields.Boolean(default=False)
    mutasi = fields.Boolean(string='Mutasi',default=False)
    lulus = fields.Boolean(string='Lulus',default=False)

    @api.depends('rombels')
    def _compute_rombel(self):
        for rec in self:
            print('inside loop compute')
            ta_aktif = self.env['siswa_ocb11.tahunajaran'].search([('active','=',True)])
            rombel_aktif = rec.rombels.search([('siswa_id','=',rec.id),('tahunajaran_id','=',ta_aktif.id)])
            # pprint(rec.rombels)
            rec.active_rombel_id = rombel_aktif.rombel_id
            print(rec.name)
    
    @api.model
    def create(self, vals):
        if vals.get('induk', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['induk'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('siswa.ocb11') or _('New')
            else:
                vals['induk'] = self.env['ir.sequence'].next_by_code('siswa.ocb11') or _('New')

        result = super(siswa, self).create(vals)
        return result


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
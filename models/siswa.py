# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from pprint import pprint
from datetime import datetime, date


class siswa(models.Model):
    _inherit = 'res.partner'

    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Diterima', required=False, ondelete="restrict")
    induk = fields.Char(string='No. Induk', required=False, copy=False, readonly=True, default="New")
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
    non_aktif_selection = fields.Selection([('mutasi', 'Mutasi'), ('lulus', 'Lulus'), ('meninggal', 'Meninggal Dunia')], string='Keterangan')
    tanggal_non_aktif = fields.Date('Tanggal Non Aktif')
    anak_ke = fields.Integer('Anak ke')
    dari_bersaudara = fields.Integer('Dari Bersaudara')
    usia = fields.Float('Usia', compute="_compute_usia")
    is_siswa_lama = fields.Boolean('Siswa Lama', default=False)
    tahunajaran_non_aktif_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran Non Aktif")

    def print_biodata(self):
        print(self.name)
        return self.env.ref('siswa_ocb11.report_biodata_siswa_action').report_action(self)

    @api.depends('tanggal_lahir')
    def _compute_usia(self):
        for rec in self:
            print(type(rec.tanggal_lahir))
            # if rec.tanggal_lahir:
            #     print(rec.tanggal_lahir.strftime('%Y/%m/%d'))
        # for rec in self:
        #     if rec.tanggal_lahir:
        #         born = date(rec.tanggal_lahir)
        #         today = date.today()
        #         usia = today.year - born.year - int((today.month, today.day) < (born.month, born.day))
        #         # print('Usia : ' + str(usia))
    
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

    @api.model
    def set_default_domain_user(self):
        # get res_id
        action_obj = self.env['ir.model.data'].search([
            ('name','=','action_res_users')
            ])

        # update domain 
        self.env['ir.actions.act_window'].search([
            ('id', '=', action_obj[0].res_id)
        ]).write({
            'domain' : "[('login','!=','root')]",
            'context' : "{'search_default_no_share': 1, 'default_tz':'Asia/Jakarta'}",
        })

        # update timezone root user
        root_user = self.env['res.users'].search([
            ('login','=','root')
        ])

        self.env.cr.execute("update res_partner set tz = 'Asia/Jakarta' where id = " + str(root_user[0].partner_id.id))
    
    @api.multi
    def toggle_active(self):
        res = super(siswa, self).toggle_active()
        if self.active:
            print('Active kan rombel siswa')
            # active kan di rombel siswa
            # self.env['siswa_ocb11.rombel_siswa'].search([
            #     ('siswa_id', '=', self.id),
            #     ('rombel_id', '=', self.active_rombel_id.id),
            # ]).write({
            #     'active' : True
            # })

            self.env.cr.execute("update siswa_ocb11_rombel_siswa set active = 'True' where siswa_id = '" + str(self.id) + "' and rombel_id = " + str(self.active_rombel_id.id) )
            # self.env.cr.fetchall()

        return res
    
    @api.multi
    def write(self, vals):
        
        pprint(vals)
        if 'rombels' in vals:
            # update jumlah siswa di rombel tersebut
            # get rombel id
            vals['rombels']
            
        result = super(siswa, self).write(vals)
        return result 
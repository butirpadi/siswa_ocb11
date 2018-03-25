# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahunajaran(models.Model):
	_name = 'siswa_ocb11.tahunajaran'

	name = fields.Char(string="Nama", required=True)
	active = fields.Boolean(default=False)
	rombels = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='tahunajaran_id')

	@api.multi
	def write(self, values):
		self.ensure_one()
		if 'active' in values:
			if values['active']:
				self.env['siswa_ocb11.tahunajaran'].search([('id', '!=', self.id)]).write({'active':False})
				# cr.execute('update siswa_ocb11_tahunajaran set active = True where id != ' + self.id)
				# print('update tahunajaran')
		result = super(tahunajaran, self).write(values)
		return result

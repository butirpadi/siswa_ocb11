# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahunajaran(models.Model):
	_name = 'siswa_ocb11.tahunajaran'

	name = fields.Char(string="Nama", required=True)
	active = fields.Boolean(default=False)
	rombels = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='tahunajaran_id')
	jenjangs = fields.One2many('siswa_ocb11.tahunajaran_jenjang', inverse_name='tahunajaran_id' , string='Jenjang', ondelete='cascade')

	@api.multi
	def write(self, values):
		for rec in self:
			if 'active' in values:
				if values['active']:
					rec.env['siswa_ocb11.tahunajaran'].search([('id', '!=', self.id)]).write({'active':False})
		result = super(tahunajaran, self).write(values)
		return result

	@api.model
	def create(self, vals):
		result = super(tahunajaran, self).create(vals)
	# 	# auto generate tahunajaran_jenjang
		print(str(result.name) + ' PG')
		self.env['siswa_ocb11.tahunajaran_jenjang'].create({
			'name' : str(result.name) + ' PG',
			'tahunajaran_id' : result.id,
			'jenjang' : 0
		})
		print(str(result.name) + ' TK A')
		self.env['siswa_ocb11.tahunajaran_jenjang'].create({
			'name' : str(result.name) + ' TK A',
			'tahunajaran_id' : result.id,
			'jenjang' : 1
		})
		print(str(result.name) + ' TK B')
		self.env['siswa_ocb11.tahunajaran_jenjang'].create({
			'name' : str(result.name) + ' TK B',
			'tahunajaran_id' : result.id,
			'jenjang' : 2
		})
		return result

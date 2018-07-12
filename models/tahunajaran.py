# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint

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
		jenjangs = self.env['siswa_ocb11.jenjang'].search([('name','ilike','%')])
		print('Generating tahunajaran_jenjang : ')
		pprint(jenjangs)
		for jj in jenjangs:
			print('Jenjang ' + jj.name)
			self.env['siswa_ocb11.tahunajaran_jenjang'].create({
				'name' : str(result.name) + ' ' + jj.name,
				'tahunajaran_id' : result.id,
				'jenjang_id' : jj.id
			})
		
		# generate dashboard rombel
		rombels = self.env['siswa_ocb11.rombel'].search([('name','ilike','%')])
		for rb in rombels:
			if rb.is_show_on_dashboard:
				# create roimbel dashboard
				self.env['siswa_ocb11.rombel_dashboard'].create({
                    'rombel_id' : rb.id,
                    'tahunajaran_id' : result.id,
                    })


		# print(str(result.name) + ' PG')
		# self.env['siswa_ocb11.tahunajaran_jenjang'].create({
		# 	'name' : str(result.name) + ' PG',
		# 	'tahunajaran_id' : result.id,
		# 	'jenjang' : 1
		# })
		# print(str(result.name) + ' TK A')
		# self.env['siswa_ocb11.tahunajaran_jenjang'].create({
		# 	'name' : str(result.name) + ' TK A',
		# 	'tahunajaran_id' : result.id,
		# 	'jenjang' : 2
		# })
		# print(str(result.name) + ' TK B')
		# self.env['siswa_ocb11.tahunajaran_jenjang'].create({
		# 	'name' : str(result.name) + ' TK B',
		# 	'tahunajaran_id' : result.id,
		# 	'jenjang' : 3
		# })
		return result

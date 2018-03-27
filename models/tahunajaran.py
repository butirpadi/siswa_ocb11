# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahunajaran(models.Model):
	_name = 'siswa_ocb11.tahunajaran'

	name = fields.Char(string="Nama", required=True)
	active = fields.Boolean(default=False)
	rombels = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='tahunajaran_id')

	@api.multi
	def write(self, values):
		for rec in self:
			if 'active' in values:
				if values['active']:
					rec.env['siswa_ocb11.tahunajaran'].search([('id', '!=', self.id)]).write({'active':False})
		result = super(tahunajaran, self).write(values)
		return result

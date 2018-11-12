# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from pprint import pprint


class tahunajaran(models.Model):
	_name = 'siswa_ocb11.tahunajaran'

	name = fields.Char(string="Nama", required=True)
	active = fields.Boolean(default=False)
	rombels = fields.One2many('siswa_ocb11.rombel_siswa', inverse_name='tahunajaran_id')
	jenjangs = fields.One2many('siswa_ocb11.tahunajaran_jenjang', inverse_name='tahunajaran_id' , string='Jenjang', ondelete='cascade')
	sort_order = fields.Integer('Order')

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
		# set order
		taj = self.env['siswa_ocb11.tahunajaran'].search([])
		print('Jumlah Tahunajaran : ' + str(len(taj)))
		if len(taj) > 0:
			# get max order				
			self.env.cr.execute('select max(sort_order) from siswa_ocb11_tahunajaran')
			max_order = self.env.cr.fetchone()			
			vals['sort_order'] = max_order[0] + 1
		else:
			vals['sort_order'] = 1

		result = super(tahunajaran, self).create(vals)

	# 	# auto generate tahunajaran_jenjang
		jenjangs = self.env['siswa_ocb11.jenjang'].search([('name', 'ilike', '%')])
		print('----------------------------------------')
		print('Generating tahunajaran_jenjang : ')
		print('----------------------------------------')
		for jj in jenjangs:
			tahunajaran_jenjang_ids = self.env['siswa_ocb11.tahunajaran_jenjang'].search([('tahunajaran_id', '=', result.id),
																						('jenjang_id', '=', jj.id)])
			if not tahunajaran_jenjang_ids:
				self.env['siswa_ocb11.tahunajaran_jenjang'].create({
					'name' : str(result.name) + ' ' + jj.name,
					'tahunajaran_id' : result.id,
					'jenjang_id' : jj.id
				})
# 		# pprint(jenjangs)
# 		for jj in jenjangs:
# 			print('Jenjang ' + jj.name)
# 			self.env['siswa_ocb11.tahunajaran_jenjang'].create({
# 				'name' : str(result.name) + ' ' + jj.name,
# 				'tahunajaran_id' : result.id,
# 				'jenjang_id' : jj.id
# 			})
		
		# generate dashboard rombel
		print('----------------------------------------')
		print('Generate rombel Dashboard')
		print('----------------------------------------')
		rombels = self.env['siswa_ocb11.rombel'].search([('name', 'ilike', '%')])
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

	def shift_up(self):
		if self.sort_order > 1:
			# get prev item
			ta_prev = self.env['siswa_ocb11.tahunajaran'].search([
				('sort_order', '=', self.sort_order - 1)
			])

			# update prev sort_order
			ta_prev.write({
				'sort_order' : self.sort_order
			})

			# update mine sort_order
			self.write({
				'sort_order' : self.sort_order - 1
			})
	
	def shift_down(self):
		self.env.cr.execute('select max(sort_order) from siswa_ocb11_tahunajaran')
		max_order = self.env.cr.fetchone()			
		if self.sort_order < max_order[0]:
			# get next item
			ta_next = self.env['siswa_ocb11.tahunajaran'].search([
				('sort_order', '=', self.sort_order + 1)
			])

			# update prev sort_order
			ta_next.write({
				'sort_order' : self.sort_order
			})

			# update mine sort_order
			self.write({
				'sort_order' : self.sort_order + 1
			})

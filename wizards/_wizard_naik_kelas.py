from flectra import models, fields, api
from pprint import pprint

class wizard_naik_kelas(models.TransientModel):
    _name = 'siswa_ocb11.wizard_naik_kelas'

    name = fields.Char('Kenaikan Kelas')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", required=True)
    next_tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran Kenaikan", required=True)
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang', string='Jenjang')
    next_jenjang_id = fields.Many2one('siswa_ocb11.jenjang', string='Jenjang Kenaikan')
    siswa_ids = fields.One2many('siswa_ocb11.wizard_naik_kelas_siswa_rel', inverse_name='wizard_id', string='Siswa')

     
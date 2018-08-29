# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import locale
import logging
import re
from operator import itemgetter

from odoo import api, fields, models, tools, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError, ValidationError


class Lang(models.Model):
    _inherit = "res.lang"

    @api.model
    def update_date_format_to_id_format(self):
        print('--------------------------------')
        print('Update Default Date Format')
        self.env.cr.execute("update res_lang set date_format = '%d/%m/%Y' where active = 'true'")
        print('done')
        print('--------------------------------')
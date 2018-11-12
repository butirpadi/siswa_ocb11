from flectra import api, fields, models, tools, _

class Currency(models.Model):
    _inherit = "res.currency"

    @api.model
    def set_active_rupiah_only(self):

        self.env.cr.execute("update res_currency set active = 'false' where name = 'EUR'")
        self.env.cr.execute("update res_currency set active = 'false' where name = 'USD'")
        self.env.cr.execute("update res_currency set active = 'true' where name = 'IDR'")
        idr_currency_id = self.env['res.currency'].search([
            ('name', '=', 'IDR')
        ])

        # set default currency to rupiah
        self.env.cr.execute("update res_company set currency_id = " + str(idr_currency_id[0].id)) 
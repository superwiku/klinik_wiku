from odoo import api, fields, models


class Pegawai(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_pegawai = fields.Boolean(string='pegawai', default=True)
    

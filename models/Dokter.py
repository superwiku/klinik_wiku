from odoo import api, fields, models


class Dokter(models.Model):
    _name = 'klinikwiku.dokter'
    _description = 'Dokter'

    name = fields.Char(string="Nama")


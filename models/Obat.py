from odoo import api, fields, models


class Obat(models.Model):
    _name = 'klinikwiku.obat'
    _description = 'New Description'

    name = fields.Char(string='Nama Obat')
    harga_satuan = fields.Integer(string='Harga Satuan')
    satuan = fields.Char(string='Satuan')
    stok = fields.Integer(string='Stok')
    
    
    

from odoo import api, fields, models


class Pembelian(models.Model):
    _name = 'klinikwiku.pembelian'
    _description = 'New Description'

    name = fields.Char(string='Name')
    tgl = fields.Datetime(string='Tangga Pembelian', default=fields.Datetime.now())
    obatnya = fields.Many2one(comodel_name='klinikwiku.obat', string='Obatnya')
    quantity = fields.Integer(string='Quantity')
    harga_satuan = fields.Char(string='Harga Satuan')
    satuan = fields.Char(string='Satuan')  
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')
    
    @api.depends('obatnya','quantity')
    def _compute_total_harga(self):
        for record in self:
            record.total_harga = record.obatnya.harga_satuan * record.quantity
    
    @api.onchange('obatnya')
    def _onchange_obatnya(self):
        self.harga_satuan = str(self.obatnya.harga_satuan) + " rupiah"
    
    @api.onchange('obatnya')
    def _onchange_obatnya_lagi(self):
        self.satuan = self.obatnya.satuan
    
    @api.model
    def create(self, vals):
        record = super(Pembelian, self).create(vals)
        if record.quantity:
            self.env['klinikwiku.obat'].search([('id','=',record.obatnya.id)]).write({'stok':record.obatnya.stok - record.quantity})
            return record
from odoo import api, fields, models


class Beli_Bahan(models.Model):
    _name = 'toko.beli_bahan'
    _description = 'Beli Bahan'

    name = fields.Char(string='Name')
    vendor_id = fields.Many2one(comodel_name='toko.vendor', string='Vendor')
    gudang_id = fields.Many2one(
                comodel_name='toko.gudang', 
                string='Bahan',
                domain=[('ls_bahan','=',True)])
    tgl_beli = fields.Date(string='Tgl Beli', default=fields.Date.today())
    qty = fields.Integer(string='Qty')
    harga = fields.Integer(string='Harga Satuan')
    total_harga = fields.Char(compute='_compute_total_harga', string='Total')
    
    @api.depends('total_harga')
    def _compute_total_harga(self):
        for record in self:
            record.total_harga = record.qty * record.harga
    
    @api.model
    def create(self, vals):
        record = super(Beli_Bahan, self).create(vals)
        if record.qty:
            self.env['toko.gudang'].search([('id', '=', record.gudang_id.id)]).write({'stock': record.gudang_id.stock + record.qty})
            return record
    
    

from odoo import api, fields, models


class Gudang(models.Model):
    _name = 'toko.gudang'
    _description = 'Gudang'

    name = fields.Char(string='Nama')
    stock = fields.Integer(string='Stock')
    harga = fields.Integer(string='Harga Satuan')
    total_buat = fields.Integer(string='Total Buat')
    total_terjual = fields.Integer(string='Total Terjual')
    ls_kue = fields.Boolean(string='List Kue', default=False)
    ls_bahan = fields.Boolean(string='List Bahan', default=False)


    jenis = fields.Char(compute='_compute_jenis', string='Jenis')

    @api.depends('ls_kue', 'ls_bahan')
    def _compute_jenis(self):
        for record in self:
            if record.ls_kue:
                record.jenis = 'Kue'
            elif record.ls_bahan:
                record.jenis = 'Bahan'
            else:
                record.jenis = 'Bahan Makanan gk Jelas'
    
    
    

    

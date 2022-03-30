from odoo import api, fields, models


class Buat_Kue(models.Model):
    _name = 'toko.buat_kue'
    _description = 'Buat Kue'

    bahan_baku_ids = fields.One2many(comodel_name='toko.bahan_produksi', inverse_name='buat_kue_id', string='Bahan Kue')
    

    name = fields.Char(string='Nama')
    chef_id = fields.Many2one(comodel_name='toko.chef', string='Chef')
    tgl_buat = fields.Date(string='Tgl Buat', default=fields.Date.today())
    qty = fields.Integer(string='Qty')
    harga_jual = fields.Integer(string='Harga Satuan')
    total_produksi = fields.Integer(compute='_compute_total_produksi')
    
    @api.depends('bahan_baku_ids')
    def _compute_total_produksi(self):
        for record in self:
            record.total_produksi = record.qty * record.bahan_baku_ids.harga_total

class Bahan_Produksi(models.Model):
    _name = 'toko.bahan_produksi'
    _description = 'Bahan Produksi'

    buat_kue_id = fields.Char(string='Bahan Kue')
    gudang_id = fields.Many2one(comodel_name='toko.gudang', string='Gudang')
    qty = fields.Integer(string='Qty')
    harga_satuan = fields.Char(compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('gudang_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.gudang_id.harga

    harga_total = fields.Char(compute='_compute_harga_total', string='Harga Total')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga_total(self):
        for record in self:
            record.harga_total = record.harga_satuan * record.qty

    @api.model
    def create(self, vals):
        record = super(Bahan_Produksi, self).create(vals)
        if record.qty:
            self.env['toko.gudang'].search([('id', '=', record.gudang_id.id)]).write({'stock': record.gudang_id.stock-record.qty})
            return record
    


    
    

    

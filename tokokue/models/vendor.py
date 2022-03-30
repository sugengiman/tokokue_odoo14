from odoo import api, fields, models


class Vendor(models.Model):
    _name = 'toko.vendor'
    _description = 'List Vendor'

    name = fields.Char(string='Nama')
    no_telp = fields.Char(string='No Telephone')
    alamat = fields.Char(string='Alamat')

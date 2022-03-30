from odoo import api, fields, models


class Customer(models.Model):
    _name = 'toko.customer'
    _description = 'List Customer'

    name = fields.Char(string='Nama')
    no_telp = fields.Char(string='No Telephone')
    alamat = fields.Char(string='Alamat')

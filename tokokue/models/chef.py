from odoo import api, fields, models


class chef(models.Model):
    _name = 'toko.chef'
    _description = 'Daftar Chef'

    name = fields.Char(string='Nama')
    no_telp = fields.Char(string='No Telephone')
    alamat = fields.Char(string='Alamat')
    cost = fields.Integer(string='Salary')
    
    

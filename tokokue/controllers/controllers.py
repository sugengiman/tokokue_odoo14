# -*- coding: utf-8 -*-
# from odoo import http


# class Tokokue(http.Controller):
#     @http.route('/tokokue/tokokue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tokokue/tokokue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tokokue.listing', {
#             'root': '/tokokue/tokokue',
#             'objects': http.request.env['tokokue.tokokue'].search([]),
#         })

#     @http.route('/tokokue/tokokue/objects/<model("tokokue.tokokue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tokokue.object', {
#             'object': obj
#         })

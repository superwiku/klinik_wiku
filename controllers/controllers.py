# -*- coding: utf-8 -*-
# from odoo import http


# class Klinikwiku(http.Controller):
#     @http.route('/klinikwiku/klinikwiku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/klinikwiku/klinikwiku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('klinikwiku.listing', {
#             'root': '/klinikwiku/klinikwiku',
#             'objects': http.request.env['klinikwiku.klinikwiku'].search([]),
#         })

#     @http.route('/klinikwiku/klinikwiku/objects/<model("klinikwiku.klinikwiku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('klinikwiku.object', {
#             'object': obj
#         })

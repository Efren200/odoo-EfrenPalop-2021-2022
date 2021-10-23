# -*- coding: utf-8 -*-
# from odoo import http


# class Proyecteprova(http.Controller):
#     @http.route('/proyecteprova/proyecteprova/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecteprova/proyecteprova/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecteprova.listing', {
#             'root': '/proyecteprova/proyecteprova',
#             'objects': http.request.env['proyecteprova.proyecteprova'].search([]),
#         })

#     @http.route('/proyecteprova/proyecteprova/objects/<model("proyecteprova.proyecteprova"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecteprova.object', {
#             'object': obj
#         })

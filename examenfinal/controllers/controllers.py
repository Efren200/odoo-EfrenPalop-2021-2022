# -*- coding: utf-8 -*-
# from odoo import http


# class Examenfinal(http.Controller):
#     @http.route('/examenfinal/examenfinal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examenfinal/examenfinal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examenfinal.listing', {
#             'root': '/examenfinal/examenfinal',
#             'objects': http.request.env['examenfinal.examenfinal'].search([]),
#         })

#     @http.route('/examenfinal/examenfinal/objects/<model("examenfinal.examenfinal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examenfinal.object', {
#             'object': obj
#         })

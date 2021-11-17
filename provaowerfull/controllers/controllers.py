# -*- coding: utf-8 -*-
# from odoo import http


# class Provaowerfull(http.Controller):
#     @http.route('/provaowerfull/provaowerfull/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/provaowerfull/provaowerfull/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('provaowerfull.listing', {
#             'root': '/provaowerfull/provaowerfull',
#             'objects': http.request.env['provaowerfull.provaowerfull'].search([]),
#         })

#     @http.route('/provaowerfull/provaowerfull/objects/<model("provaowerfull.provaowerfull"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('provaowerfull.object', {
#             'object': obj
#         })

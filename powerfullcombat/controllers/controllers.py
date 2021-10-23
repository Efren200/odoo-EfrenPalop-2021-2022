# -*- coding: utf-8 -*-
# from odoo import http


# class Powerfullcombat(http.Controller):
#     @http.route('/powerfullcombat/powerfullcombat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/powerfullcombat/powerfullcombat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('powerfullcombat.listing', {
#             'root': '/powerfullcombat/powerfullcombat',
#             'objects': http.request.env['powerfullcombat.powerfullcombat'].search([]),
#         })

#     @http.route('/powerfullcombat/powerfullcombat/objects/<model("powerfullcombat.powerfullcombat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('powerfullcombat.object', {
#             'object': obj
#         })

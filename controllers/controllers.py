# -*- coding: utf-8 -*-
from odoo import http

# class YfcUpdate(http.Controller):
#     @http.route('/yfc_update/yfc_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yfc_update/yfc_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yfc_update.listing', {
#             'root': '/yfc_update/yfc_update',
#             'objects': http.request.env['yfc_update.yfc_update'].search([]),
#         })

#     @http.route('/yfc_update/yfc_update/objects/<model("yfc_update.yfc_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yfc_update.object', {
#             'object': obj
#         })
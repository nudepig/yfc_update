# -*- coding: utf-8 -*-
from odoo import http

class YfcUpdate(http.Controller):
    @http.route('/yfc_update/yfc_update/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/yfc_update/yfc_update/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('yfc_update.listing', {
            'root': '/yfc_update/yfc_update',
            'objects': http.request.env['yfc_update.yfc_update'].search([]),
        })

    @http.route('/yfc_update/yfc_update/objects/<model("yfc_update.yfc_update"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('yfc_update.object', {
            'object': obj
        })

# from odoo.addons.website_sale.controllers.main import WebsiteSale
# from odoo.http import request
# import werkzeug.utils
#
#
# class ResWebsiteSale(WebsiteSale):
#
#     @http.route([
#         '''/shop''',
#         '''/shop/page/<int:page>''',
#         '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
#         '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
#     ], type='http', auth="public", website=True)
#     def shop(self, page=0, category=None, search='', ppg=False, **post):
#         # auroral 2020-5-25
#         if not request.session.uid:
#             return werkzeug.utils.redirect('/web/login')
#         # auroral 2020-5-25
#         return super(ResWebsiteSale, self).shop(page, category, search, ppg, **post)
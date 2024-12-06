# -*- coding: utf-8 -*-
# from odoo import http


# class AddonsUstadam/sincsolLmsAddCourse(http.Controller):
#     @http.route('/addons_ustadam/sincsol_lms_add_course/addons_ustadam/sincsol_lms_add_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons_ustadam/sincsol_lms_add_course/addons_ustadam/sincsol_lms_add_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons_ustadam/sincsol_lms_add_course.listing', {
#             'root': '/addons_ustadam/sincsol_lms_add_course/addons_ustadam/sincsol_lms_add_course',
#             'objects': http.request.env['addons_ustadam/sincsol_lms_add_course.addons_ustadam/sincsol_lms_add_course'].search([]),
#         })

#     @http.route('/addons_ustadam/sincsol_lms_add_course/addons_ustadam/sincsol_lms_add_course/objects/<model("addons_ustadam/sincsol_lms_add_course.addons_ustadam/sincsol_lms_add_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons_ustadam/sincsol_lms_add_course.object', {
#             'object': obj
#         })


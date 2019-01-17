# -*- coding: utf-8 -*-
from odoo import http

class Openacademy(http.Controller):

    #view index
    @http.route('/openacademy/index/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"

    #view all course
    @http.route('/openacademy/course/', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('openacademy.course', {
            'root': '/openacademy/course',
            'objects': http.request.env['openacademy.course'].search([]),
        })

    @http.route('/openacademy/course/<model("openacademy.course"):obj>/', auth='public', website=True)
    def object(self, obj, **kw):
        id=obj.id
        sessions=http.request.env['openacademy.session']
        sessions=sessions.search([])
        sessions = sessions.filtered(lambda r: r.course_id == r.id)
        # sessions=sessions.sorted(course_id=lambda r: r.id)
        # sessions=sessions.filtered(lambda r: r.course_id == obj.id)
        # list=[]
        # for session in sessions:
        #     if session.course_id == obj.id:


        # object=http.request.env['openacademy.object']
        # return http.request.render('openacademy.object',object)

        return http.request.render('openacademy.object', {
                    'object': obj, 'sessions':sessions, 'id':id
                })
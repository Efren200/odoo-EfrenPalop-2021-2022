# -*- coding: utf-8 -*-
from odoo import models, fields, api


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string="Nom", readonly=False, required=True, help="Aquest és el nom")
    birth_year = fields.Integer()
    description = fields.Text()
    enrollment_date = fields.Date()
    last_login = fields.Datetime()
    is_student = fields.Boolean()
    photo = fields.Image(max_width=200, max_height=200)
    classroom = fields.Many2one('school.classroom', ondelete='set null', help='La clase a la que va')
    teachers = fields.Many2many('school.teacher', related='classroom.teachers', readonly=True)

class classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Les classes'

    name = fields.Char()
    students = fields.One2many(string='Students', comodel_name='school.student', inverse_name='classroom')
    teachers = fields.Many2many(comodel_name='school.teacher',
                                relation='teachers_classrooms',
                                column1='classroom_id',
                                column2='teacher_id')
    teachers_ly = fields.Many2many(comodel_name='school.teacher',
                                relation='teachers_classrooms_ly',
                                column1='classroom_id',
                                column2='teacher_id')

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Els professors'

    name = fields.Char()
    classrooms = fields.Many2many(comodel_name='school.classroom',
                                relation='teachers_classrooms',
                                column2='classroom_id',
                                column1='teacher_id')
    classrooms_ly = fields.Many2many(comodel_name='school.classroom',
                                  relation='teachers_classrooms_ly',
                                  column2='classroom_id',
                                  column1='teacher_id')




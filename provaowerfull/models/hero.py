

from odoo import models, fields, api


class hero(models.Model):
    _name = 'provaowerfull.hero'
    _description = 'Heroes'

    name = fields.Char()
    stars = fields.Integer()
    type = fields.Char()
    attack = fields.Integer()
    defense = fields.Integer()
    health = fields.Integer()
    hero_icon = fields.Image(max_width=200, max_height=200)


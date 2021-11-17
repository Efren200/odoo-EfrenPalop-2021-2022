

from odoo import models, fields, api


class hero(models.Model):
    _name = 'provaowerfull.hero'
    _description = 'Heroes'

    name = fields.Char()
    stars = fields.Integer()
    type = fields.Selection([('1','Plant'),('2','Fire'),('3','Water')])
    attack = fields.Float()
    defense = fields.Float()
    health = fields.Float()
    hero_icon = fields.Image(max_width=200, max_height=200)


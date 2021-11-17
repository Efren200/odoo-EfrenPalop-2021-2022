

from odoo import models, fields, api


class potion(models.Model):
    _name = 'provaowerfull.potion'
    _description = 'Potions'

    name = fields.Char()
    attack_increase = fields.Float()
    defense_increase = fields.Float()
    health_increase = fields.Float()
    loquesiga = fields.Float()
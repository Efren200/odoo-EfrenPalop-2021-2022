

from odoo import models, fields, api


class potion(models.Model):
    _name = 'provaowerfull.potion'
    _description = 'Potions'

    name = fields.Char()
    attack_increase = fields.Float()
    defense_increase = fields.Float()
    health_increase = fields.Float()
    mana_price = fields.Float()
    potion_icon = fields.Image(max_width=200, max_height=200)

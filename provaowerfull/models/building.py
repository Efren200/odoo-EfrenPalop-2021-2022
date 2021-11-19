
from odoo import models, fields, api


class building(models.Model):
    _name = 'provaowerfull.building'
    _description = 'Buildings'

    name = fields.Char()
    capacity = fields.Float()
    collection_minute = fields.Float()
    building_icon = fields.Image(max_width=200, max_height=200)
    

from odoo import models, fields, api

class alliance(models.Model):
    _name = "provaowerfull.alliance"
    _description = "Alliance"

    name = fields.Char()
    players = fields.One2many(comodel_name='provaowerfull.player', inverse_name='alliance')
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets


class player(models.Model):
    _name = 'provaowerfull.player'
    _description = 'Players'

    name = fields.Char()
    password = fields.Char(default=lambda s:secrets.token_urlsafe(10))
    level = fields.Integer(default=1)
    gold = fields.Integer(default=1000)
    mana = fields.Integer(default=1000)
    gems = fields.Integer(default=0)
    trophies = fields.Integer(default=0)
    icon = fields.Image(max_width=200, max_height=200)
    registration_date = fields.Datetime()
    heroes = fields.Many2many('provaowerfull.hero')
    potions = fields.Many2many('provaowerfull.potion')
    buildings = fields.Many2many('provaowerfull.building')








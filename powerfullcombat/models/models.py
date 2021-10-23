# -*- coding: utf-8 -*-

from odoo import models, fields, api

class player(models.Model):
    _name = 'powerfullcombat.player'
    _description = 'Players'

    name = fields.Char(string="Name", readonly=False, required=True, help="Player name")
    level = fields.Integer(default=1)
    gold = fields.Integer(default=1000)
    mana = fields.Integer(default=1000)
    gems = fields.Integer(default=0)
    trophies = fields.Integer(default=0)
    heroes = fields.One2many(string='Heroes', comodel_name='powerfullcombat.hero', inverse_name='player')
    potions = fields.One2many(string='Potions', comodel_name='proyecteprova.potion', inverse_name='player')
    collector_buildings = fields.One2many(string='Collector Buildings', comodel_name='powerfullcombat.collector_building', inverse_name='player')
    storage_buildings = fields.One2many(string='Storage Buildings', comodel_name='powerfullcombat.storage_building', inverse_name='player')
    buildings = fields.One2many(string='Buildings', comodel_name='powerfullcombat.building', inverse_name='player')
class hero(models.Model):
    _name = 'powerfullcombat.hero'
    _description = "Hero"

    name = fields.Char(string="Name", readonly=False, required=True, help="Hero name")
    type = fields.Char(string="Type", readonly=False, required=True, help="Hero type")
    stars = fields.Integer(required=True, help="Hero stars")
    attack = fields.Integer(required=True, help="Hero attack")
    defense = fields.Integer(required=True, help="Hero defense")
    health = fields.Integer(required=True, help="Hero health")
    photo = fields.Image(max_width=200, max_height=300)
    player = fields.Many2one(comodel_name='powerfullcombat.player', ondelete='set null', help='Player who has the hero')

class potion(models.Model):
    _name = 'powerfullcombat.potion'
    _description = "Potion"

    name = fields.Char(string="Name", readonly=False, required=True, help="Potion name")
    attack_increase = fields.Integer(required=True, help="Potion attack increase")
    defense_increase = fields.Integer(required=True, help="Potion defense increase")
    health_increase = fields.Integer(required=True, help="Potion health increase")
    player = fields.Many2one(comodel_name='powerfullcombat.player', ondelete='set null', help='Player who has the potion')

class collector_building(models.Model):
    _name = 'powerfullcombat.collector_building'
    _description = "Collector building"

    name = fields.Char(string="Name", readonly=False, required=True, help="Collector building name")
    level = fields.Integer(default=1)
    reward_Minute = fields.Integer(default=10)
    capacity = fields.Integer(default=1000)
    price = fields.Integer(default=200)
    player = fields.Many2one(comodel_name='powerfullcombat.player', ondelete='set null', help='Collector buildings that the player has')


class storage_building(models.Model):
    _name = 'powerfullcombat.storage_building'
    _description = "Storage building"

    name = fields.Char(string="Name", readonly=False, required=True, help="Storage building name")
    level = fields.Integer(default=1)
    capacity = fields.Integer(default=1000)
    price = fields.Integer(default=200)
    player = fields.Many2one(comodel_name='powerfullcombat.player', ondelete='set null', help='Storage buildings that the player has')

class building(models.Model):
    _name = 'powerfullcombat.building'
    _description = "Building"

    name = fields.Char(string="Name", readonly=False, required=True, help="Building name")
    level = fields.Integer(default=1)
    price = fields.Integer()
    player = fields.Many2one(comodel_name='powerfullcombat.player', ondelete='set null', help='Buildings that the player has')

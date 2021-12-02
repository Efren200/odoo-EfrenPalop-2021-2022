# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
import random
from odoo.exceptions import ValidationError


class player(models.Model):
    _name = 'provaowerfull.player'
    _description = 'Players'

    name = fields.Char(required=True)
    password = fields.Char(default=lambda s:secrets.token_urlsafe(10))
    level = fields.Integer(default=1)
    resources_capacity = fields.Integer(compute='_get_res_capacity')
    gold = fields.Integer(default=1000)
    mana = fields.Integer(default=1000)
    gems = fields.Integer(default=0)
    trophies = fields.Integer(default=0)
    icon = fields.Image(max_width=200, max_height=200)
    last_connection = fields.Date()
    heroes = fields.Many2many('provaowerfull.hero')
    quantity_heroes = fields.Integer(compute='_get_q_heroes')
    potions = fields.One2many('provaowerfull.potionplayer', 'player')
    quantity_potions = fields.Integer(compute='_get_q_potions')
    buildings = fields.One2many('provaowerfull.buildingplayer', 'player')
    quantity_buildings = fields.Integer(compute='_get_q_buildings')
    alliance = fields.Many2one('provaowerfull.alliance' ,ondelete='set null', help='Alliance to which the player belongs')


    
    #Restriccion para controlar cuantos recursos tiene el usuario.
    @api.constrains('gold', 'mana', 'gems', 'resources_capacity')
    def _check_resources(self):
        for p in self:

            if p.gold > p.resources_capacity or p.mana > p.resources_capacity or p.gems > p.resources_capacity :

                raise ValidationError('You cant have more resources than you can store')


    #Metodo para saber cual sera la capacidad maxima de recursos que podra tener el player
    @api.depends('level')
    def _get_res_capacity(self):
        for p in self:
                p.resources_capacity = p.level * p.level * 1000

    #Metodo para contar cuantos heroes tiene el player
    @api.depends('heroes')
    def _get_q_heroes(self):
        for p in self:
                p.quantity_heroes = len(p.heroes)

    #Metodo para contar cuantas construcciones tiene el player
    @api.depends('buildings')
    def _get_q_buildings(self):
        for p in self:
                p.quantity_buildings = len(p.buildings)

    #Funcion para generar un heroe aleatorio
    def random_hero(self):
        for p in self:
            random_prob = random.randint(1, 100)

            if p.quantity_heroes < 100 :
                if random_prob > 0 and random_prob < 40:
                    hero_id = random.choice(self.env['provaowerfull.hero'].search([('stars','=',1)]).ids)

                elif random_prob > 40 and random_prob < 65:
                    hero_id = random.choice(self.env['provaowerfull.hero'].search([('stars','=',2)]).ids)

                elif random_prob > 65 and random_prob < 85:
                    hero_id = random.choice(self.env['provaowerfull.hero'].search([('stars','=',3)]).ids)

                elif random_prob > 85 and random_prob < 97:
                    hero_id = random.choice(self.env['provaowerfull.hero'].search([('stars','=',4)]).ids)
            
                else:
                    hero_id = random.choice(self.env['provaowerfull.hero'].search([('stars','=',5)]).ids)

                p.write({'heroes': [(4,hero_id,0)]})
            
            else:
                raise ValidationError('You cannot have more than 100 heroes. Delete some')


    #Metodo para contar cuantos heroes tiene el player
    @api.depends('potions')
    def _get_q_potions(self):
        for p in self:
            p.quantity_potions = len(p.potions)


    #Funcion para poder comprar una pocion pequeña
    def buy_small_potion(self):
        for p in self:

            if p.quantity_potions < 20 :
                potion = self.env['provaowerfull.potion'].search([('name','=','Small Potion')])
                if p.mana >= potion.mana_price :
                    p.mana = p.mana - potion.mana_price
                    self.env['provaowerfull.potionplayer'].create({'player':p.id,'potion': potion.id})
                else:
                    raise ValidationError('You dont have enough mana to buy the item')
            else:
                raise ValidationError('You cannot have more than 20 potions. Delete some')

    #Funcion para poder comprar una pocion grande
    def buy_big_potion(self):
        for p in self:

            if p.quantity_potions < 20 :
                potion = self.env['provaowerfull.potion'].search([('name','=','Big Potion')])
                if p.mana >= potion.mana_price :
                    p.mana = p.mana - potion.mana_price
                    self.env['provaowerfull.potionplayer'].create({'player':p.id,'potion': potion.id})
                else:
                    raise ValidationError('You dont have enough mana to buy the item')
            else:
                raise ValidationError('You cannot have more than 20 potions. Delete some')

    
    #Funcion para poder comprar una pocion de ataque
    def buy_attack_potion(self):
        for p in self:

            if p.quantity_potions < 20 :
                potion = self.env['provaowerfull.potion'].search([('name','=','Attack Potion')])
                if p.mana >= potion.mana_price :
                    p.mana = p.mana - potion.mana_price
                    self.env['provaowerfull.potionplayer'].create({'player':p.id,'potion': potion.id})
                else:
                    raise ValidationError('You dont have enough mana to buy the item')
            else:
                raise ValidationError('You cannot have more than 20 potions. Delete some')

    #Funcion para poder comprar una pocion de ataque
    def buy_defense_potion(self):
        for p in self:

            if p.quantity_potions < 20 :
                potion = self.env['provaowerfull.potion'].search([('name','=','Defense Potion')])
                if p.mana >= potion.mana_price :
                    p.mana = p.mana - potion.mana_price
                    self.env['provaowerfull.potionplayer'].create({'player':p.id,'potion': potion.id})
                else:
                    raise ValidationError('You dont have enough mana to buy the item')
            else:
                raise ValidationError('You cannot have more than 20 potions. Delete some')

    #Funcion para poder comprar una mina de oro
    def buy_gold_mine(self):
        for p in self:

            if p.quantity_buildings < 6 :
                building = self.env['provaowerfull.building'].search([('name','=','Gold Mine')])
                if p.gold >= building.gold_price :
                    p.gold = p.gold - building.gold_price
                    self.env['provaowerfull.buildingplayer'].create({'player':p.id,'building': building.id, 'level': 1, 
                                            'name': building.name, 'collection_minute': building.collection_minute, 'capacity': building.capacity,
                                             'gold_price': building.gold_price})
                else:
                    raise ValidationError('You dont have enough gold to buy the item')
            else:
                raise ValidationError('You cannot have more than 6 buildings. Delete some')

    #Funcion para poder comprar un collector de mana
    def buy_mana_collector(self):
        for p in self:
            if p.quantity_buildings < 6 :
                building = self.env['provaowerfull.building'].search([('name','=','Mana Collector')])
                if p.gold >= building.gold_price :
                    p.gold = p.gold - building.gold_price
                    self.env['provaowerfull.buildingplayer'].create({'player':p.id,'building': building.id, 'level': 1, 
                                            'name': building.name, 'collection_minute': building.collection_minute, 'capacity': building.capacity,
                                             'gold_price': building.gold_price})
                else:
                    raise ValidationError('You dont have enough gold to buy the item')
            else:
                raise ValidationError('You cannot have more than 6 buildings. Delete some')

    #Funcion para poder comprar una mina de gemas
    def buy_gem_mine(self):
        for p in self:
            if p.quantity_buildings < 6 :
                building = self.env['provaowerfull.building'].search([('name','=','Gem Mine')])
                if p.gold >= building.gold_price :
                    p.gold = p.gold - building.gold_price
                    self.env['provaowerfull.buildingplayer'].create({'player':p.id,'building': building.id, 'level': 1, 
                                            'name': building.name, 'collection_minute': building.collection_minute, 'capacity': building.capacity,
                                             'gold_price': building.gold_price})
                else:
                    raise ValidationError('You dont have enough gold to buy the item')
            else:
                raise ValidationError('You cannot have more than 6 buildings. Delete some')


        #Funcion para poder comprar una pocion de ataque
    def level_up(self):
        for p in self:
            level_price = p.level*p.level*1000
            if p.gold >= level_price  :
                p.gold = p.gold - level_price
                
                p.level = p.level + 1
            else:
                raise ValidationError('You cannot have money to get the level up')


            





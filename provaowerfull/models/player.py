# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
import random
from odoo.exceptions import ValidationError

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
    quantity_heroes = fields.Integer(compute='_get_q_heroes')
    potions = fields.Many2many('provaowerfull.potion')
    quantity_potions = fields.Integer(compute='_get_q_potions')
    buildings = fields.Many2many('provaowerfull.building')



    #Metodo para contar cuantos heroes tiene el player
    @api.depends('heroes')
    def _get_q_heroes(self):
        for p in self:
                p.quantity_heroes = len(p.heroes)

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
                potion_id = self.env['provaowerfull.potion'].search([('name','=','Small Potion')])
                if p.mana >= potion_id.mana_price :
                    p.mana = p.mana - potion_id.mana_price
                    p.write({'potions': [(4,potion_id,0)]})
                else:
                    raise ValidationError('You dont have enough mana to buy the item')
            else:
                raise ValidationError('You cannot have more than 20 potions. Delete some')

            





from odoo import models, fields, api
from odoo.exceptions import ValidationError

class potionplayer(models.Model):
    _name = 'provaowerfull.battles'
    _description = 'Battles'

    player1 = fields.Many2one('provaowerfull.player', required=True)
    p1_name = fields.Char(related="player1.name")
    player2 = fields.Many2one('provaowerfull.player', required=True)
    p2_name = fields.Char(related="player2.name")

    p1_hero1 = fields.Many2one('provaowerfull.hero', required=True)
    p1_hero2 = fields.Many2one('provaowerfull.hero', required=True)   
    p1_hero3 = fields.Many2one('provaowerfull.hero', required=True)

    p2_hero1 = fields.Many2one('provaowerfull.hero', required=True)  
    p2_hero2 = fields.Many2one('provaowerfull.hero', required=True)
    p2_hero3 = fields.Many2one('provaowerfull.hero', required=True)  

    p1_potion = fields.Many2one('provaowerfull.potionplayer')
    p2_potion = fields.Many2one('provaowerfull.potionplayer')

    winner_name = fields.Char()


    #Restriccion para que el player 1 no sea el player 2
    @api.constrains('player1', 'player2')
    def check_players(self):
        for b in self:
            if b.player1.id == b.player2.id :
                raise ValidationError('The two players cannot be the same')

    #Restriccion para que los heroes del player sean todos diferentes
    @api.constrains('p1_hero1', 'p1_hero2', 'p1_hero3', 'p2_hero1', 'p2_hero2', 'p2_hero3')
    def check_players(self):
        for b in self:
            if b.p1_hero1.id == b.p1_hero2.id or b.p1_hero1.id == b.p1_hero3.id or b.p1_hero2.id == b.p1_hero3.id :
                raise ValidationError('You cant fight a repeat hero')

            elif b.p2_hero1.id == b.p2_hero2.id or b.p2_hero1.id == b.p2_hero3.id or b.p2_hero2.id == b.p2_hero3.id :
                raise ValidationError('You cant fight a repeat hero')


    @api.onchange('player1')
    def _onchange_player1(self):
        if self.player1 != False:
            heroes = self.player1.heroes
            potions = self.player1.potions
            return{
                'domain':{
                    'p1_hero1': [('id', 'in', heroes.ids)],
                    'p1_hero2': [('id', 'in', heroes.ids)],
                    'p1_hero3': [('id', 'in', heroes.ids)],
                    'p1_potion': [('id', 'in', potions.ids)]
                }
            }

    @api.onchange('player2')
    def _onchange_player2(self):
        if self.player2 != False:
            heroes = self.player2.heroes
            potions = self.player2.potions
            return{
                'domain':{
                    'p2_hero1': [('id', 'in', heroes.ids)],
                    'p2_hero2': [('id', 'in', heroes.ids)],
                    'p2_hero3': [('id', 'in', heroes.ids)],
                    'p2_potion': [('id', 'in', potions.ids)]
                }
            }



    #Funcion para generar una batalla entre dos players con sus heroes y pociones
    def battle_between_players(self):
        ganador_p1 = False
        ganador_p2 = False
        health_p1 = self.p1_hero1.health  + self.p1_hero2.health  + self.p1_hero3.health + self.p1_potion.health_increase
        attack_p1 = self.p1_hero1.attack  + self.p1_hero2.attack  + self.p1_hero3.attack + self.p1_potion.attack_increase
        defense_p1 = self.p1_hero1.defense  + self.p1_hero2.defense  + self.p1_hero3.defense + self.p1_potion.defense_increase

        health_p2 = self.p2_hero1.health  + self.p2_hero2.health  + self.p2_hero3.health + self.p2_potion.health_increase
        attack_p2 = self.p2_hero1.attack  + self.p2_hero2.attack  + self.p2_hero3.attack + self.p2_potion.attack_increase
        defense_p2 = self.p2_hero1.defense  + self.p2_hero2.defense  + self.p2_hero3.defense + self.p2_potion.defense_increase

        while health_p2 > 0 and health_p1 > 0:
            health_p1 -=  attack_p2 - defense_p1 
            health_p2 -= attack_p1 - defense_p2

            print("Vida restante: " + health_p1)
            print("Vida restante: " + health_p2)
            if health_p1 <=0:
                ganador_p2 = True

            elif health_p2 <= 0:
                ganador_p1 = True

        if(ganador_p1):
            self.winner_name = self.p1_name
            self.player1.trophies += 10

        if(ganador_p2):
            self.winner_name = self.p2_name
            self.player2.trophies += 10

        if self.p1_potion != None:
            self.p1_potion.unlink()
        
        if self.p2_potion != None:
            self.p2_potion.unlink()

        

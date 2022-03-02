from odoo import models, fields, api
from odoo.exceptions import ValidationError

class battles(models.Model):
    _name = 'provaowerfull.battles'
    _description = 'Battles'

    player1 = fields.Many2one('res.partner')
    p1_name = fields.Char(related="player1.name")
    player2 = fields.Many2one('res.partner')
    p2_name = fields.Char(related="player2.name")

    p1_hero1 = fields.Many2one('provaowerfull.hero')
    p1_hero2 = fields.Many2one('provaowerfull.hero')   
    p1_hero3 = fields.Many2one('provaowerfull.hero')

    p2_hero1 = fields.Many2one('provaowerfull.hero')  
    p2_hero2 = fields.Many2one('provaowerfull.hero')
    p2_hero3 = fields.Many2one('provaowerfull.hero')  

    p1_potion = fields.Many2one('provaowerfull.potionplayer')
    p2_potion = fields.Many2one('provaowerfull.potionplayer')

    winner_name = fields.Char()


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

class hero_transient(models.TransientModel):
    _name = 'provaowerfull.hero_transient'

    hero = fields.Many2one('provaowerfull.hero')
    imagen = fields.Image(related='hero.hero_icon')


    def selectp1(self):
        wizard = self._context.get('battles_wizard_context')
        wizard = self.env['provaowerfull.battles_wizard'].browse(wizard)

        wizard.write({'heroes1': [(4,self.hero.id,0)]})
        return {
            'name': 'PowerfullCombat battle wizard action',
            'type': 'ir.actions.act_window',
            'res_model': wizard._name,
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
            'context': wizard._context
        }

    def selectp2(self):
        wizard = self._context.get('battles_wizard_context')
        wizard = self.env['provaowerfull.battles_wizard'].browse(wizard)

        wizard.write({'heroes2': [(4,self.hero.id,0)]})
        return {
            'name': 'PowerfullCombat battle wizard action',
            'type': 'ir.actions.act_window',
            'res_model': wizard._name,
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
            'context': wizard._context
        }

class battles_wizard(models.TransientModel):
    _name = 'provaowerfull.battles_wizard'
    _description = 'Wizard of Battles'

    player1 = fields.Many2one('res.partner')
    p1_name = fields.Char(related="player1.name")
    player2 = fields.Many2one('res.partner')
    p2_name = fields.Char(related="player2.name")

    heroes1 = fields.Many2many(comodel_name='provaowerfull.hero', relation="heroesfirstplayer")
    heroes2 = fields.Many2many(comodel_name='provaowerfull.hero', relation="heroessecondplayer")
    heroes_aviable1 = fields.Many2many('provaowerfull.hero_transient', compute="_get_heroes_aviable1")
    heroes_aviable2 = fields.Many2many('provaowerfull.hero_transient', compute="_get_heroes_aviable2")

    winner_name = fields.Char()
    

    @api.depends('player1')
    def _get_heroes_aviable1(self):
        heroes = self.env['provaowerfull.hero_transient']
        self.heroes_aviable1 = heroes


        heroes_aviable1 = self.player1.heroes

            
        for hero in heroes_aviable1:
            heroes = heroes + self.env['provaowerfull.hero_transient'].create({'hero': hero.id})


        self.heroes_aviable1 = heroes

    @api.depends('player2')
    def _get_heroes_aviable2(self):
        heroes = self.env['provaowerfull.hero_transient']
        self.heroes_aviable2 = heroes


        heroes_aviable2 = self.player2.heroes

            
        for hero in heroes_aviable2:
            heroes = heroes + self.env['provaowerfull.hero_transient'].create({'hero': hero.id})


        self.heroes_aviable2 = heroes

    

    #Funcion para generar una batalla entre dos players con sus heroes y pociones
    def battle_between_players_wizard(self):
        ganador_p1 = False
        ganador_p2 = False
        health_p1 = 0
        attack_p1 = 0
        defense_p1 = 0
        health_p2 = 0
        attack_p2 = 0
        defense_p2 = 0
        for herop1 in self.heroes_aviable1:
            health_p1 = health_p1 + herop1.hero.health
            attack_p1 = attack_p1 + herop1.hero.attack
            defense_p1 = defense_p1 + herop1.hero.defense 

        for herop2 in self.heroes_aviable2:
            health_p2 = health_p2 + herop2.hero.health
            attack_p2 = attack_p2 + herop2.hero.attack
            defense_p2 = defense_p2 + herop2.hero.defense

        while health_p2 > 0 and health_p1 > 0:
            health_p1 -=  attack_p2 - defense_p1 
            health_p2 -= attack_p1 - defense_p2

            if health_p1 <=0:
                ganador_p2 = True

            elif health_p2 <= 0:
                ganador_p1 = True

        if(ganador_p1):
            trophies = self.player1.trophies + 10
            self.player1.write({'trophies': trophies})

            self.winner_name = self.p1_name


        if(ganador_p2):

            trophies = self.player2.trophies + 10
            self.player2.write({'trophies': trophies})

            self.winner_name = self.p2_name

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }


    
    state = fields.Selection([('1', 'PLayer1'),('2', 'PLayer2'), ('3', 'Battle'),('4', 'Battle Result')], default='1')


    def next(self):
        if self.state == '1':
            self.state = '2'
        elif self.state == '2':
            self.state = '3'
        elif self.state == '3':
            self.state = '4'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

        
    def previous(self):
        if self.state == '2':
            self.state = '1'
        elif self.state == '3':
            self.state = '2'
        elif self.state == '4':
            self.state = '3'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }


    @api.model
    def action_generate_battle(self):
        action = self.env.ref('provaowerfull.action_generate_battle').read()[0]
        return action


    #Acabar
    def create_battle(self):
        battle = self.env['provaowerfull.battles'].create({
            'player1': self.player1.id,
            'player2' : self.player2.id,
            'p1_name': self.player1.name,
            'p2_name' : self.player2.name,
            'winner_name': self.winner_name,
        })
        return {
            'name': 'PowerfullCombat Battle',
            'type': 'ir.actions.act_window',
            'res_model': 'provaowerfull.battles',
            'res_id': battle.id,
            'view_mode': 'form',
            'target': 'current'
        }
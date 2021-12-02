from odoo import models, fields, api

class potionplayer(models.Model):
    _name = 'provaowerfull.potionplayer'
    _description = 'Potion / Player'

    player = fields.Many2one('provaowerfull.player', ondelete='set null')
    player_name = fields.Char(related="player.name")
    potion = fields.Many2one('provaowerfull.potion', ondelete='set null')
    potion_icon = fields.Image(related="potion.potion_icon")
    name = fields.Char(related="potion.name")
    attack_increase = fields.Float(related="potion.attack_increase")
    defense_increase = fields.Float(related="potion.defense_increase")
    health_increase = fields.Float(related="potion.health_increase")
    mana_price = fields.Float(related="potion.mana_price")

    #Funcion para borrar una pocion propia del player 
    def delete_potionplayer(self):
        self.unlink()

    
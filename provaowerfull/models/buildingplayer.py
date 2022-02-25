from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class buildingplayer(models.Model):
    _name = 'provaowerfull.buildingplayer'
    _description = 'Building / Player'

    player = fields.Many2one('res.partner', ondelete='set null')
    player_name = fields.Char(related="player.name")
    building = fields.Many2one('provaowerfull.building', ondelete='set null')
    name = fields.Char(related="building.name")
    building_icon = fields.Image(related="building.building_icon")
    gold_price = fields.Integer()
    level = fields.Integer(default=1)

    capacity = fields.Float()
    collection_minute = fields.Float()
    actual_capacity = fields.Float()
            

    #Funcion para borrar un edificio propio del player 
    def delete_buildingplayer(self):
        self.unlink()


    #Funcion para mejorar una construccion
    def update_buildingplayer(self):
        
        upgrade_price = self.gold_price * 2

        if self.player.level > self.level : 

            if self.player.gold >= upgrade_price : 
                self.player.gold = self.player.gold - upgrade_price
                self.level = self.level + 1
                self.collection_minute = self.collection_minute + self.collection_minute 
                self.capacity = self.capacity + self.capacity
            else:
                raise ValidationError('You dont have enough gold to upgrade the building')
        else:
            raise ValidationError('You dont have enough level to upgrade the building')



    #Funcio para poder recollir els materials creats
    @api.model
    def recollection(self):


        buildings = self.search([])

        for b in buildings:

            if(b.actual_capacity < b.capacity):
            
                b.actual_capacity = b.actual_capacity + b.collection_minute
            

    def recolectar(self):

        if self.actual_capacity >= self.capacity:

            if self.building.name == "Gold Mine" :

                self.player.gold  = self.player.gold + self.actual_capacity
                self.actual_capacity = 0

            elif self.building.name == "Mana Collector" :

                self.player.mana  = self.player.mana + self.actual_capacity
                self.actual_capacity = 0

            else:
                self.player.mana  = self.player.mana + self.actual_capacity
                self.actual_capacity = 0
        else:
            raise ValidationError('El recollector no esta lleno')      







        




from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class buildingplayer(models.Model):
    _name = 'provaowerfull.buildingplayer'
    _description = 'Building / Player'

    player = fields.Many2one('provaowerfull.player', ondelete='set null')
    player_name = fields.Char(related="player.name")
    building = fields.Many2one('provaowerfull.building', ondelete='set null')
    name = fields.Char(related="building.name")
    capacity = fields.Float()
    collection_minute = fields.Float()
    gold_price = fields.Integer()
    level = fields.Integer(default=1)
    time = fields.Float(compute='_get_time')
    date_start = fields.Datetime()
    date_end = fields.Datetime(compute='_get_time')
    progress = fields.Float()

    state = fields.Selection([('unfinished','Unfinished'),('inprogress','In Progress'),('finished','Finished')])

    
    @api.depends('date_start')
    def _get_time(self):  
        for bp in self:
            if bp.state != 'finished':

                bp.time = bp.level * bp.level
                remaining_percent = 100 - bp.progress
                remaining_time = remaining_percent * bp.time /100

                if bp.date_start:
                    bp.date_end = fields.Datetime.to_string(fields.Datetime.from_string(fields.datetime.now()) + timedelta(hours=remaining_time))
                else:
                    bp.date_end = ''
            
            else:
                bp.date_end = False
                bp.time = 0

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
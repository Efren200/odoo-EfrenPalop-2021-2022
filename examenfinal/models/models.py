# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
import random
from odoo.exceptions import ValidationError


class clients(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    #_description = 'Players'

    #name = fields.Char(required=True)

    songs = fields.Many2many('examenfinal.songs')
    

class songs(models.Model):
    _name = 'examenfinal.songs'
    _description = "Songs"
    
    name = fields.Char()
    artist = fields.Char()
    popularity = fields.Integer()
    clients = fields.Many2many('res.partner')
    
    
    @api.model
    def update_popularity(self):
        
        songs = self.search([])

        for s in songs:
    
            s.popularity = s.popularity - 1
            
class client_wizard(models.TransientModel):
    
    _name = 'examenfinal.client_wizard'
    
    def _get_client(self):

        print("Cliente")
        return self._context.get('active_id')
        
       
        
    
    song = fields.Many2one('examenfinal.songs')
    client = fields.Many2one('res.partner', default=_get_client )
    


    
    @api.model
    def action_client_wizard(self):
        
        action = self.env.ref('examenfinal.action_client_wizard')
        return action
    
    def save_song(self):
        
        self.client.songs = self.client.songs + self.song
        self.song.popularity = self.song.popularity + 100
        
        return {
            'name': 'ExamenFinal Songs',
            'type': 'ir.actions.act_window',
            'res_model': 'examenfinal.songs',
            'res_id': self.song.id,
            'view_mode': 'form',
            'target': 'current'
        }
        


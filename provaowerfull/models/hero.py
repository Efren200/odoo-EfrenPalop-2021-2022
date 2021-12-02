

from odoo import models, fields, api


class hero(models.Model):
    _name = 'provaowerfull.hero'
    _description = 'Heroes'

    name = fields.Char()
    stars = fields.Integer()
    type = fields.Char() #He intentat fer un Selection pero no me apareixen les dades
    attack = fields.Integer()
    defense = fields.Integer()
    health = fields.Integer()
    hero_icon = fields.Image(max_width=100, max_height=100)
    players = fields.Many2many('provaowerfull.player')



    #Funcion para borrar un heroe seleccionado
    def delete_hero(self):
        for h in self:
            player = self.env['provaowerfull.player'].browse(self.env.context['player'])
            player.write({'heroes': [(3,h.id,0)]})


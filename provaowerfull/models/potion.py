

from odoo import models, fields, api


class potion(models.Model):
    _name = 'provaowerfull.potion'
    _description = 'Potions'

    name = fields.Char()
    attack_increase = fields.Float()
    defense_increase = fields.Float()
    health_increase = fields.Float()
    mana_price = fields.Float()
    potion_icon = fields.Image(max_width=200, max_height=200)

    #Funcion para borrar una pocion seleccionado
    def delete_potion(self):
        for p in self:
            player = self.env['provaowerfull.player'].browse(self.env.context['player'])
            player.write({'potions': [(3,p.id,0)]})

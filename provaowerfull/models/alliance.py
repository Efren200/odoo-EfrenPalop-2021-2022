from odoo import models, fields, api
from odoo.exceptions import ValidationError

class alliance(models.Model):
    _name = "provaowerfull.alliance"
    _description = "Alliance"

    name = fields.Char(required=True)
    players = fields.One2many(comodel_name='res.partner', inverse_name='alliance')

    player1 = fields.Many2one('res.partner')
    player2 = fields.Many2one('res.partner')

    p1_potion = fields.Many2one('provaowerfull.potionplayer')
    p2_potion = fields.Many2one('provaowerfull.potionplayer')

    all_trophies = fields.Integer(compute='_get_q_trophies')

    @api.depends('players')
    def _get_q_trophies(self):
        for a in self:
            contador = 0
            for p in a.players:
                contador = p.trophies + contador
            a.all_trophies = contador


    @api.onchange('player1')
    def _onchange_player1(self):
        if self.player1 != False:
            potions = self.player1.potions
            return{
                'domain':{
                    'p1_potion': [('id', 'in', potions.ids)]
                }
            }

    @api.onchange('player2')
    def _onchange_player2(self):
        if self.player2 != False:
            potions = self.player2.potions
            return{
                'domain':{
                    'p2_potion': [('id', 'in', potions.ids)]
                }
            }



    #Funcion para generar una batalla entre dos players con sus heroes y pociones
    def exchanges_between_players(self):

        self.p1_potion.player = self.player2.id
        self.p2_potion.player = self.player1.id
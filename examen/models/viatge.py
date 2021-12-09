from odoo import models, fields, api
from odoo.exceptions import ValidationError


class viatge(models.Model):
    _name = 'examen.viatge'
    _description = 'Viatges'

    conductor = fields.Many2one("res.partner")
    identificador = fields.Integer()
    furgoneta = fields.Many2one('examen.furgoneta', ondelete="set null")
    paquets = fields.One2many('examen.paquet', 'viatges')
    
    @api.constrains('paquets')
    def _check_resources(self):
        for v in self:
            suma = 0
            for paquet in v.paquets:
                print(paquet.volum)
                suma += paquet.volum

            print(suma)
            if suma > v.furgoneta.capacitat :
                raise ValidationError('No te caben mas paquetes en la furgoneta que corresponde al viaje')
                
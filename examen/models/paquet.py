
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class paquet(models.Model):
    _name = 'examen.paquet'
    _description = 'Paquets'

    identificador = fields.Char()
    volum = fields.Float()
    viatges = fields.Many2one("examen.viatge", ondelete="set null")



    @api.constrains('viatges')
    def _check_resources(self):
        for p in self:
            suma = 0
            for paquet in p.viatges.paquets:
                print(paquet.volum)
                suma += paquet.volum

            print(suma)
            if suma > p.viatges.furgoneta.capacitat :
                raise ValidationError('No te caben mas paquetes en la furgoneta que corresponde al viaje')





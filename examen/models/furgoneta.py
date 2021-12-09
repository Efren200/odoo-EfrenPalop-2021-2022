from odoo import models, fields, api


class furgoneta(models.Model):
    _name = 'examen.furgoneta'
    _description = 'Furgonetes'

    name = fields.Char()
    capacitat = fields.Float()
    image = fields.Image()
    viatges = fields.One2many('examen.viatge', "furgoneta" )

    paquets = fields.Many2many('examen.paquet', compute="_get_paquets")


    @api.depends('viatges')
    def _get_paquets(self):
        lista = []
        for f in self:
            for v in f.viatges:
                for p in v.paquets:
                    print(p)
                    lista.append(p.id)
                    print(lista)
            
            f.paquets = lista
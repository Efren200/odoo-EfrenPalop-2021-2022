# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
import base64


class edifici(models.Model):
    _name = 'imatges.edifici'
    name = fields.Char()

    def _get_default_image(self):
        with open(modules.get_module_resource('imatges', 'static/src/img', 'demo.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    foto = fields.Image(default=_get_default_image, max_width=200, max_height=200)
    tipus = fields.Selection([('1', 'Hotel'), ('2', 'Hotel'), ('3 ', 'Institut')])


from odoo import models, fields, api

from datetime import datetime, timedelta


class player_premium(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_premium = fields.Boolean()
    date_end = fields.Datetime()

    def apply_premium(self,time):
        if self.is_premium:
            end = fields.Datetime.from_string(self.date_end)
            new_end = end + timedelta(minutes=time)
            self.date_end = fields.Datetime.to_string(new_end)


        else:
            new_end = datetime.now() + timedelta(minutes=time)
            self.date_end = fields.Datetime.to_string(new_end)
            self.is_premium = True

            for bp in self.buildings:

                bp.collection_minute *= 2


    @api.model
    def check_premium(self):
        players = self.search([('is_premium','=',True)])
        print('Premium Cron', players)
        for p in players:
            if p.date_end < fields.Datetime.now():
                p.is_premium = False




class product_premium(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    is_premium = fields.Boolean(default=False)

    minutes_premium = fields.Integer()


class sale_premium(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    premium_applied = fields.Boolean(default=False)

    def apply_premium(self):

        premium_products = self.order_line.filtered(lambda p: p.product_id.is_premium == True and self.premium_applied == False)
        for p in premium_products:
            self.partner_id.apply_premium(p.product_id.minutes_premium)

    def write(self,values):
        super(sale_premium,self).write(values)
        self.apply_premium()

    @api.model
    def create(self,values):
        record = super(sale_premium,self).create(values)
        record.apply_premium()
        return record


class pedido(models.Model):

    _name = 'provaowerfull.pedido'

    name = fields.Char()

    player = fields.Many2one('res.partner', required=True)

    producto = fields.Many2one('product.product', compute='_get_product')



    def _get_product(self):

        producto = self.env.ref('provaowerfull.premium_product')

        self.producto = producto


class pedido_wizard(models.TransientModel):

    _name = 'provaowerfull.pedido_wizard'

    name = fields.Char()
    player = fields.Many2many('res.partner', required=True)
    producto = fields.Many2many('product.product', compute='_get_product')

    state = fields.Selection([('1', 'Sale Name'), ('2', 'Player Selection'), ('3', 'Enrollment')], default='1')


    def _get_product(self):

        producto = self.env.ref('provaowerfull.premium_product')

        self.producto = producto

    @api.model
    def action_generate_premium(self):
        action = self.env.ref('provaowerfull.action_generate_premium').read()[0]
        return action

    def create_pedido(self):

        for p in self:

           pedido = p.env['sale.order'].create({'partner_id': p.player.id})
           p.env['sale.order.line'].create({'order_id': pedido.id,'product_id': p.producto.id})

           p.env['provaowerfull.pedido'].create({'player': p.player.id, 'producto': p.producto.id, 'name': p.name})
           p.player.apply_premium(p.producto.minutes_premium)

    def next(self):
        if self.state == '1':
            self.state = '2'
        elif self.state == '2':
            self.state = '3'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
    
    def previous(self):
        if self.state == '2':
            self.state = '1'
        elif self.state == '3':
            self.state = '2'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }


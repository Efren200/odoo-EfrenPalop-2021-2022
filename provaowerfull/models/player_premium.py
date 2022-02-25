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
# -*- coding: utf-8 -*-
from odoo import http


class banner_premium_controller(http.Controller):
    @http.route('/provaowerfull/pedido', auth='user', type='json')

    def banner(self):
        return {
            'html': """
                <div  class="player_banner" style="height: 200px; background-size:100%">
                    <link href="provaowerfull/static/src/css/banner.css" rel="stylesheet">

                    <h1>Hazte Premium</h1>
                    <a class="player_button" type="action" data-reload-on-close="true" 
                    role="button" data-method="action_generate_premium" data-model="provaowerfull.pedido_wizard">Make Premium</a>
                    
                </div> """
        }

    

class banner_battles_controller(http.Controller):
    @http.route('/provaowerfull/batalla', auth='user', type='json')

    def banner(self):
        return {
            'html': """
                <div  class="batalla_banner" style="height: 200px; background-size:100%">
                    <link href="provaowerfull/static/src/css/banner.css" rel="stylesheet">

                    <h1>Make our Battles</h1>
                    <a class="batalla_button" type="action" data-reload-on-close="true" 
                    role="button" data-method="action_generate_battle" data-model="provaowerfull.battles_wizard">Start Battle</a>
                    
                </div> """
        }    


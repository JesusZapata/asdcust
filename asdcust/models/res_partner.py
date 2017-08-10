from odoo import models


class Partner(models.Model):

    _inherit = "res.partner"

    _sql_constraints = [
        ('name_res_partner', 'unique (name)', 'The name of the company can be'
         'not repeated!')
    ]

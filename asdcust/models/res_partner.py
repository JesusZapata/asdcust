from odoo import models, fields, api


class Partner(models.Model):

    _inherit = "res.partner"

    _sql_constraints = [
        ('name_res_partner', 'unique (name)', 'The name of the company can be'
         'not repeated!')
    ]

    repeated_name = fields.Char(compute='_name_repeated', store=True)

    def _name_repeated(self):
        for record in self:
            record.write({'name': 'Agrolait'})


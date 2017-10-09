# coding: utf-8

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    test = fields.Char()
    change = fields.Char()

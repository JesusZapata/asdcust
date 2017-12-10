# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Partner(models.Model):

    _inherit = 'res.partner'

    test_name = fields.Char(string='Title')

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        default['test_name'] = _('TestName')
        default['test_name'] = _('NewTranslatable')

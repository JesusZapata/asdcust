# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Partner(models.Model):

    test_name = fields.Char(string='Title', required=True)

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        default['test'] = _('Test')

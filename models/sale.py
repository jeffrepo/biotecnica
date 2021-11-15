# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    municipio_id = fields.Many2one('biotecnica.municipio', store=True)

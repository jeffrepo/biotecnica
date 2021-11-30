# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    municipio_id = fields.Many2one('biotecnica.municipio', string="Municipio",store=True)
    validar_orden = fields.Boolean('Validar orden', copy=False)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        municipio_id = False
        if self.partner_id and self.partner_id.municipio_id:
            municipio_id = self.partner_id.municipio_id
            self.municipio_id = municipio_id.id

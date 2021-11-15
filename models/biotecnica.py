# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BiotecnicaMunicipio(models.Model):
    _name = 'biotecnica.municipio'

    name = fields.Char('Nombre')

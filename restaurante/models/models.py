# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plato(models.Model):
    _name='restaurante.plato'
    _description="Plato de restaurante"

    name=fields.Char(string="Titulo",required=True)
    description=fields.Text()

class Carta(models.Model): 
    _name = 'restaurante.carta' 
    _description = "Menu de restaurante" 
    
    name = fields.Char(string="Title", required=True) 
    description = fields.Text() 
    start_date = fields.Date() 
    duration = fields.Float(digits=(6, 2), help="Activo en días") 
    calorias = fields.Integer(string="Calorías")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)

    

# class restaurante(models.Model):
#     _name = 'restaurante.restaurante'
#     _description = 'restaurante.restaurante'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

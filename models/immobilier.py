from odoo import models, fields, api

class Immobilier(models.Model):
    _name = 'immobilier' 
    _description = 'Gestion des biens immobiliers'

    description = fields.Text(string="Description", required=True)
    adresse = fields.Text(string="Adresse complète")
    prix = fields.Float(string="Prix de location",required=True)
    bailleur_id = fields.Many2one(
        'partenaire', 
        string="Bailleur",
        domain="[('type_part', '=', 'b')]"
    )
    date_dispo = fields.Date(string="Date de disponibilité")
    louer = fields.Boolean(string="Actif", default=True)
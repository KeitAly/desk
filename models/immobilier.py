from odoo import models, fields, api

class Immobilier(models.Model):
    _name = 'immobilier'  # Doit correspondre à model_immobilier
    _description = 'Gestion des biens immobiliers'

    name = fields.Char(string="Référence", required=True)
    adresse = fields.Text(string="Adresse complète")
    prix = fields.Float(string="Prix de location")
    bailleur_id = fields.Many2one(
        'partenaire', 
        string="Bailleur",
        domain="[('type_part', '=', 'b')]"  # Filtre uniquement les bailleurs
    )
    date_dispo = fields.Date(string="Date de disponibilité")
    active = fields.Boolean(string="Actif", default=True)
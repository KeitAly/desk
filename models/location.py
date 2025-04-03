from odoo import models, fields,api
from datetime import date
from dateutil.relativedelta import relativedelta

class Location(models.Model):
    _name = 'location' 
    _description = 'Gestion des locations'

    immobilier_id = fields.Many2one(
        'immobilier', 
        string="Bien immobilier", 
        required=True, 
        domain=[('louer','=',True)],

        ondelete='cascade'
    )  
    locataire_id = fields.Many2one(
        'partenaire', 
        string="Locataire", 
        domain=[('type_part', '=', 'l'),('supprimer','=',False)],  
        required=True
    )  
    bailleur_id = fields.Many2one(
        'partenaire', 
        string="Bailleur", 
        domain=[('type_part', '=', 'b'),('supprimer','=',False)], 
        related='immobilier_id.bailleur_id', 
        store=True
    )
    duree_location = fields.Integer(string="Durée de la location (en mois)", required=True, store=True)
    date_debut = fields.Date(string="Date de début", required=True) 
    date_fin = fields.Date(string="Date de fin",store=True)  
    montant_loyer = fields.Float(string="Montant de la location",store=True) 
   
   #Calculer automatiquement la date de fin basée sur la date de début et la durée de la locatio
    @api.onchange('date_debut', 'duree_location','Simmobilier_id')
    def _compute_date_fin(self):
      
        if self.date_debut and self.duree_location:
            
            self.date_fin = fields.Date.to_string(
                fields.Date.from_string(self.date_debut) + relativedelta(months=self.duree_location)
            )
        if self.immobilier_id:
                self.montant_loyer = self.immobilier_id.prix * self.duree_location



#function pour modifier le champs active d'un immbilier après location 
    @api.model
    def create(self, values):
        immobilier = self.env['immobilier'].browse(values['immobilier_id'])
        if immobilier.louer: 
            immobilier.louer = False
        return super(Location, self).create(values)

    @api.depends('date_debut', 'date_fin')
    def _compute_active_status(self):
        for record in self:
            immobilier = record.immobilier_id
            # Si la date actuelle est dans la période de location, le bien doit être inactif
            if record.date_debut <= date.today() <= record.date_fin:
                immobilier.louer = False
            else:
                immobilier.louer = True

  

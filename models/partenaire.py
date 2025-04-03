from odoo import models, fields,api


class Partenaire(models.Model):
    _name='partenaire'
    _description=' les locataires et les bailleurs associé de l\'entreprise '
    _rec_name = 'display_name'

    type_part = fields.Selection(selection=[('l','Locataire'),('b','Bailleur')],string="Type",default="l")
    nom = fields.Char(string="Nom",required=True)
    prenom = fields.Char(string="Prénom",required=True)
    tel = fields.Char(string="Téléphone",required=True)
    adress = fields.Char(string="Adresse")
    supprimer = fields.Boolean(string="supprimer",default=False)
        # Champ calculé pour afficher le nom complet
    display_name = fields.Char(string='Nom complet', compute='_compute_display_name', store=False)

    @api.depends('nom', 'prenom')
    def _compute_display_name(self):
        for record in self:
            # Combine first_name et last_name pour créer le nom complet
            record.display_name = f"{record.nom} {record.prenom}"


   #funtion pour mettre le partenaire en etat de supprimer
    def supression(self):
        for ligne in self:
            ligne.write({'supprimer':True})


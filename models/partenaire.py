from odoo import models, fields


class Partenaire(models.Model):
    _name='partenaire'
    _description=' les locataires et les bailleurs associé de l\'entreprise '

    type_part = fields.Selection(selection=[('l','Locataire'),('b','Bailleur')],string="Type",default="l")
    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénom")
    tel = fields.Char(string="Téléphone")
    adress = fields.Char(string="Adresse")
    supprimer = fields.Boolean(string="supprimer",default=False)

    def supression(self):
        for ligne in self:
            ligne.write({'supprimer':True})

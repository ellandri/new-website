from db import Database
from datetime import datetime


class Personne:
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone):
        self.id = id
        self.dateNaissance = dateNaissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def supprimer(self, id):
        db = Database()
        query = "DELETE FROM eleve WHERE id = %s"
        db.execute_query(query, (id,))
        db.close()

    

    def lister(self):
        db = Database()
        query = "SELECT * FROM personne"
        return db.fetch_query(query)

    

class Education:
    def enseigner(self, matiere):
        return f"Enseigne la matière {matiere}"

    def preparerCours(self, cours):
        return f"Prépare le contenu d'un cours sur le sujet {cours}"

    def assisterReunion(self, sujet):
        return f"Doit assister à une reunion sur {sujet}"

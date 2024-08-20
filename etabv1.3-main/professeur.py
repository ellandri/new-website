from personne import Personne
from db import Database



class Professeur(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.vacant = vacant
        self.matiereEnseigne = matiereEnseigne
        self.prochainCours = prochainCours
        self.sujetProchaineReunion = sujetProchaineReunion

    def ajouter(self):
        db = Database()
        query = """INSERT INTO profeseur (id, dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        db.execute_query(query, (self.id, self.dateNaissance, self.ville, self.prenom, self.nom, self.telephone, self.vacant, self.matiereEnseigne, self.prochainCours, self.sujetProchaineReunion))
        db.close()

    def mettreAJour(self):
        db = Database()
        query = """UPDATE profeseur SET vacant = %s, matiereEnseigne = %s, prochainCours = %s, sujetProchaineReunion = %s 
                WHERE id = %s"""
        db.execute_query(query, (self.vacant, self.matiereEnseigne, self.prochainCours, self.sujetProchaineReunion, self.id))
        db.close()
        
    def supprimerprofesseur(self):
        db = Database()
        query = "DELETE FROM profeseur WHERE id = %s"
        db.execute_query(query, (id,))
        db.close()



from personne import Personne
from db import Database


class Eleve(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.classe = classe
        self.matricule = matricule

    def ajouter(self):
        db = Database()
        query = """INSERT INTO eleve (id, dateNaissance, ville, prenom, nom, telephone, classe, matricule) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        db.execute_query(query, (self.id, self.dateNaissance, self.ville, self.prenom, self.nom, self.telephone, self.classe, self.matricule))
        db.close()

    def mettreAJour(self):
        db = Database()
        query = """UPDATE eleve SET classe = %s, matricule = %s 
                WHERE id = %s"""
        db.execute_query(query, (self.classe, self.matricule, self.id))
        db.close()
        
    def supprimereleve(self):
        db = Database()
        query = "DELETE FROM eleve WHERE id = %s"
        db.execute_query(query, (self.id,))
        db.close()


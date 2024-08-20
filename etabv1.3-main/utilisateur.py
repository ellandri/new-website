from db import Database

class Utilisateur:
    def __init__(self, id, identifiant, motDePasse):
        self.id = id
        self.identifiant = identifiant
        self.motDePasse = motDePasse

    def authentification(self, identifiant, motDePasse):
        return self.identifiant == identifiant and self.motDePasse == motDePasse

    @staticmethod
    def ajouterCompte(identifiant, motDePasse):
        db = Database()
        query = "INSERT INTO utilisateur (identifiant, motDePasse) VALUES (%s, %s)"
        db.execute_query(query, (identifiant, motDePasse))
        db.close()

    @staticmethod
    def modiferMotDePasse(identifiant, motDePasse):
        db = Database()
        query = "UPDATE utilisateur SET motDePasse = %s WHERE identifiant = %s"
        db.execute_query(query, (motDePasse, identifiant))
        db.close()

    @staticmethod
    def supprimerCompte(identifiant):
        db = Database()
        query = "DELETE FROM utilisateur WHERE identifiant = %s"
        db.execute_query(query, (identifiant,))
        db.close()

    @staticmethod
    def listerUtilisateur():
        db = Database()
        query = "SELECT * FROM utilisateur"
        return db.fetch_query(query)

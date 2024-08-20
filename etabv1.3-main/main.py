from utilisateur import Utilisateur
from professeur import Professeur
from eleve import Eleve

from datetime import datetime
import time

def afficher_menu_principal():
    print("""
    ******************************************************
    BIENVENU DANS L’APPLICATION ETAB v1.3
    ******************************************************
    MENU:
    1: Gestion des élèves
    2: Gestion des professeurs
    3: Gestion des utilisateurs
    0: Quitter
    
    """)
    print(" Date système :", time.strftime("%H:%M"))

def afficher_menu_eleve():
    print("""
    ******************************************************
    GESTION DES ELEVES
    ******************************************************
    Menu :
    1: Ajouter un élève
    2: Supprimer un élève
    3: Modifier les informations de l'élève
    4: Lister les élèves
    5: Retour
    0: Quitter
    ******************************************************
    """)

def afficher_menu_professeur():
    print("""
    ******************************************************
    GESTION DES PROFESSEURS
    ******************************************************
    Menu :
    1: Ajouter un professeur
    2: Supprimer un professeur
    3: Modifier les informations du professeur
    4: Lister les professeurs
    5: Accueil
    ******************************************************
    """)

def afficher_menu_utilisateur():
    print("""
    ******************************************************
    GESTION DES UTILISATEURS
    ******************************************************
    Menu :
    1: Ajouter un utilisateur
    2: Supprimer un utilisateur
    3: Modifier le mot de passe d'un utilisateur
    4: Lister les utilisateurs
    0: Retour
    ******************************************************
    """)

def menu_principal():
    start_time = time.time()
    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option : ")
        if choix == '1':
            menu_eleve()
        elif choix == '2':
            menu_professeur()
        elif choix == '3':
            menu_utilisateur()
        elif choix == '0':
            quitter_application(start_time)
            exit()
        else:
            print("Option invalide.")

def menu_eleve():
    while True:
        afficher_menu_eleve()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_eleve()
        elif choix == '2':
            supprimer_eleve()
        elif choix == '3':
            modifier_eleve()
        elif choix == '4':
            lister_eleves()
        
        elif choix == '5':
            menu_principal()
        elif choix == '0':
            quitter_application(start_time)
            exit()
        else:
            print("Option invalide.")

def menu_professeur():
    while True:
        afficher_menu_professeur()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_professeur()
        elif choix == '2':
            supprimer_professeur()
        elif choix == '3':
            modifier_professeur()
        elif choix == '4':
            lister_professeurs()
        elif choix == '5':
            menu_principal()
        else:
            print("Option invalide.")

def menu_utilisateur():
    while True:
        afficher_menu_utilisateur()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_utilisateur()
        elif choix == '2':
            supprimer_utilisateur()
        elif choix == '3':
            modifier_mot_de_passe()
        elif choix == '4':
            lister_utilisateurs()
        elif choix == '0':
            exit()
        else:
            print("Option invalide.")

def ajouter_professeur():
    try:
        id = int(input("Entrez l'ID : "))
        date_naissance = datetime.strptime(input("Entrez Date de naissance (Année-Mois-Jour) : "), "%Y-%m-%d")
        ville = input("Entrez la Ville : ")
        prenom = input("Entrez le prénom : ")
        nom = input("Entrez le nom : ")
        telephone = input("Entrez le téléphone : ")
        vacant = input("Vacant (True/False) : ").strip().lower() == 'true'
        matiere_enseigne = input("Entrez la matière enseignée : ")
        prochain_cours = input("Entrez le prochain cours : ")
        sujet_prochaine_reunion = input("Entrez le sujet prochaine réunion : ")
        professeur = Professeur(id, date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion)
        professeur.ajouter()
        print("Entrez le professeur ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout du professeur : {e}")

def supprimer_professeur():
    try:
        id = int(input("L'ID du professeur à supprimer : "))
        professeur = Professeur(id=id, dateNaissance=None, ville=None, prenom=None, nom=None, telephone=None, vacant=None, matiereEnseigne=None, prochainCours=None, sujetProchaineReunion=None)
        professeur.supprimer(id)
        print("Le professeur supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression du professeur : {e}")

def modifier_professeur():
    try:
        id = int(input("l'ID du professeur à modifier : "))
        date_naissance = datetime.strptime(input("Nouvelle date de naissance (YYYY-MM-DD) : "), "%Y-%m-%d")
        ville = input("Entrez la Nouvelle ville : ")
        prenom = input("Entrez le Nouveau prénom : ")
        nom = input("Entrez le Nouveau nom : ")
        telephone = input("Entrez le Nouveau téléphone : ")
        vacant = input("Vacant (True/False) : ").strip().lower() == 'true'
        matiere_enseigne = input("Entrez la Nouvelle matière enseignée : ")
        prochain_cours = input("Entrez leNouveau prochain cours : ")
        sujet_prochaine_reunion = input("Entrez le Nouveau sujet prochaine réunion : ")
        professeur = Professeur(id, date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion)
        professeur.mettreAJour()
        print("Le Professeur mis à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification du professeur : {e}")

def lister_professeurs():
    try:
        professeurs = Professeur.obtenirProfesseur()
        for professeur in professeurs:
            print(professeur)
    except Exception as e:
        print(f"Erreur lors de la liste des professeurs : {e}")
        
        



def ajouter_eleve():
    try:
        id = int(input("Entrez l'ID : "))
        date_naissance = datetime.strptime(input("Entrez la Date de naissance (Année-Mois-Jour) : "), "%Y-%m-%d")
        ville = input("Entrez laVille : ")
        prenom = input("Entrez le Prénom : ")
        nom = input("Entrez le Nom : ")
        telephone = input("Entrez leTéléphone : ")
        classe = input("Entrez la Classe : ")
        matricule = input("Entrez le Matricule : ")
        eleve = Eleve(id, date_naissance, ville, prenom, nom, telephone, classe, matricule)
        eleve.ajouter()
        print("Élève ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'élève : {e}")

def supprimer_eleve():
    try:
        id = int(input("L'ID de l'élève à supprimer : "))
        eleve = Eleve(id=id, dateNaissance=None, ville=None, prenom=None, nom=None, telephone=None, classe=None, matricule=None)
        eleve.supprimer(id)
        print("Élève supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'élève : {e}")

def modifier_eleve():
    try:
        id = int(input("L'ID de l'élève à modifier : "))
        date_naissance = datetime.strptime(input("Entrez la Nouvelle date de naissance (Année-Mois-Jour) : "), "%Y-%m-%d")
        ville = input("Entrez la Nouvelle ville : ")
        prenom = input("Entrez le Nouveau prénom : ")
        nom = input("Entrez le Nouveau nom : ")
        telephone = input("Entrez Nouveau téléphone : ")
        classe = input("Entrez la Nouvelle classe : ")
        matricule = input("Entrez le Nouveau matricule : ")
        eleve = Eleve(id, date_naissance, ville, prenom, nom, telephone, classe, matricule)
        eleve.mettreAJour()
        print("Élève mis à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification de l'élève : {e}")

def lister_eleves():
    try:
        eleves = Eleve.obtenirEleve()
        for eleve in eleves:
            print(eleve)
    except Exception as e:
        print(f"Erreur!! lors de la liste des élèves : {e}")
        




def ajouter_utilisateur():
    try:
        identifiant = input("Entrez l'Identifiant : ")
        mot_de_passe = input("Entrez le Mot de passe : ")
        Utilisateur.ajouterCompte(identifiant, mot_de_passe)
        print("Utilisateur ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

def supprimer_utilisateur():
    try:
        identifiant = input("Identifiant de l'utilisateur à supprimer : ")
        Utilisateur.supprimerCompte(identifiant)
        print("Utilisateur supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'utilisateur : {e}")

def modifier_mot_de_passe():
    try:
        identifiant = input("Entrez l'Identifiant : ")
        nouveau_mot_de_passe = input("Entrez le Nouveau mot de passe : ")
        Utilisateur.modiferMotDePasse(identifiant, nouveau_mot_de_passe)
        print("Mot de passe modifié avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification du mot de passe : {e}")

def lister_utilisateurs():
    try:
        utilisateurs = Utilisateur.listerUtilisateur()
        for utilisateur in utilisateurs:
            print(utilisateur)
    except Exception as e:
        print(f"Erreur lors de la liste des utilisateurs : {e}")
        
def quitter_application(start_time):
    try:
        end_time = time.time()
        duree_session = int((end_time - start_time) / 60)
        print("Au revoir !")
        print(f"Durée de la session : {duree_session} minutes")
    except Exception as e:
        print(f"Erreur inattendue: {e}")

if __name__ == "__main__":
    identifiant = input("Identifiant : ")
    mot_de_passe = input("Mot de passe : ")
    admin = Utilisateur(id=1, identifiant='admin', motDePasse='admin')
    if admin.authentification(identifiant, mot_de_passe):
        menu_principal()
    else:
        print("Identifiant ou mot de passe incorrect")

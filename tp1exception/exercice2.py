import re

def valider_nom_prenom(nom_prenom):
    return nom_prenom.isalpha()

def valider_date_naissance(date_naissance):
    try:
        jour, mois, annee = map(int, date_naissance.split('/'))
        return 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2004
    except ValueError:
        return False

def valider_email(email):
    return re.match(r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$', email)

def valider_telephone(telephone):
    return re.match(r'^\+212\d{1,9}$', telephone)

def valider_nom_utilisateur(nom_utilisateur):
    return re.match(r'^[a-zA-Z][a-zA-Z0-9_]+$', nom_utilisateur)

def valider_mot_de_passe(mot_de_passe):
    return len(mot_de_passe) >= 8 and any(c.islower() for c in mot_de_passe) and any(c.isupper() for c in mot_de_passe) and any(c.isdigit() for c in mot_de_passe) and any(not c.isalnum() for c in mot_de_passe)

while True:
    nom = input("Entrez votre nom: ")
    prenom = input("Entrez votre prénom: ")
    date_naissance = input("Entrez votre date de naissance (jj/mm/aaaa): ")
    email = input("Entrez votre adresse e-mail: ")
    telephone = input("Entrez votre numéro de téléphone (+212XXXXXXXXX): ")
    nom_utilisateur = input("Entrez votre nom d'utilisateur: ")
    mot_de_passe = input("Entrez votre mot de passe: ")
    confirmation_mot_de_passe = input("Confirmez votre mot de passe: ")

    try:
        if (valider_nom_prenom(nom) and valider_nom_prenom(prenom) and
            valider_date_naissance(date_naissance) and
            valider_email(email) and valider_telephone(telephone) and
            valider_nom_utilisateur(nom_utilisateur) and
            valider_mot_de_passe(mot_de_passe) and
            mot_de_passe == confirmation_mot_de_passe):
            print("Formulaire valide!")
            break
        else:
            print("Erreur : Les données du formulaire ne sont pas valides. Veuillez réessayer.")
    except Exception as e:
        print("Erreur :", e)

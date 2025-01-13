class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

def lire_fichier():
    try:
        with open("C:/Users/Hicham/Desktop/SCHOOL/POO/m103_seance9/Atelier_m103_ch8_FilesIO.pdf/test3.text", "r") as fichier:
            texte = fichier.readlines()
        if not texte:
            raise FileEmpty("Le fichier est vide.")
        return texte
    except FileNotFoundError:
        raise FileNotFoundError("Fichier non trouvé.")
    except FileEmpty as fe:
        raise fe

def calculer_points(texte):
    points_par_eleve = {}
    for line in texte:
        try:
            elements = line.strip().split()
            if len(elements) != 3:
                raise BadLine("La ligne ne contient pas trois éléments.")
            prenom, nom, points_str = elements
            points = float(points_str)
            nom_complet = prenom + " " + nom
            if nom_complet in points_par_eleve:
                points_par_eleve[nom_complet] += points
            else:
                points_par_eleve[nom_complet] = points
        except ValueError:
            raise BadLine("Les points ne sont pas valides dans la ligne : " + line)
        except BadLine as bl:
            raise bl
    return points_par_eleve

def afficher_rapport(points_par_eleve):
    for eleve, points in sorted(points_par_eleve.items()):
        print(eleve, points)

try:
    texte = lire_fichier()
    points_par_eleve = calculer_points(texte)
    afficher_rapport(points_par_eleve)
except StudentsDataException as sde:
    print("Erreur :", sde)

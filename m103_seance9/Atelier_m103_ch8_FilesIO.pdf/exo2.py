def lire_fichier():
    try:
        with open(r'C:/Users/Hicham/Desktop/SCHOOL/POO/m103_seance9/Atelier_m103_ch8_FilesIO.pdf/test.text', 'rt') as fichier:
            texte = fichier.read()
        return texte
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return None

def generer_histogramme(texte):
    occurrences = {}
    for caractere in texte:
        if caractere.isalpha():  # Vérifier si le caractère est une lettre
            caractere = caractere.lower()  # Convertir en minuscule
            if caractere in occurrences:
                occurrences[caractere] += 1
            else:
                occurrences[caractere] = 1
    return occurrences

def afficher_histogramme(occurrences):
    # Trier les lettres en fonction de leur fréquence, de la plus grande à la plus petite
    for lettre in sorted(occurrences, key=lambda x: occurrences[x], reverse=True):
        print(lettre, "=>", occurrences[lettre])

texte = lire_fichier()
if texte:
    histogramme = generer_histogramme(texte)
    afficher_histogramme(histogramme)
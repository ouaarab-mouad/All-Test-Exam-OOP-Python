def filter_students(Students, taille_limite, poids_limite):
    students_filtres = {}

    for nom, (taille, poids) in Students.items():
        if taille > taille_limite and poids > poids_limite:
            students_filtres[nom] = (taille, poids)

    return students_filtres

# Exemple d'utilisation
Students = {
    'Alice': (160, 50),
    'Bob': (175, 70),
    'Charlie': (155, 45),
    'David': (180, 80)
}

taille_limite = 170
poids_limite = 65

eleves_filtres = filter_students(Students, taille_limite, poids_limite)

print("Élèves qui dépassent la taille de", taille_limite, "et le poids de", poids_limite, ":")
print(eleves_filtres)

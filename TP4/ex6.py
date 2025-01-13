#1. Pour ajouter les données d'un stagiaire dans un module donné :

def ajouter_notes(Data, module, notes):
    Data[module] = notes
    return Data


#2. Pour calculer la moyenne obtenue par le stagiaire dans un module donné :

def moyenne_module(Data, module):
    notes = Data[module]
    moyenne = sum(notes) / len(notes)
    return moyenne


#3. Pour retourner le nom du module dont le stagiaire a obtenu la moyenne la plus élevée :

def module_moyenne_plus_elevee(Data):
    moyennes = {}
    for module in Data:
        moyennes[module] = moyenne_module(Data, module)
    module_plus_elevee = max(moyennes, key=moyennes.get)
    return module_plus_elevee


#4. Pour retourner le nom du module dans lequel le stagiaire a obtenu la moyenne la plus faible :

def module_moyenne_plus_faible(Data):
    moyennes = {}
    for module in Data:
        moyennes[module] = moyenne_module(Data, module)
    module_plus_faible = min(moyennes, key=moyennes.get)
    return module_plus_faible


#5. Pour retourner la moyenne générale (de tous les modules) obtenue par le stagiaire :

def moyenne_generale(Data):
    moyennes = []
    for module in Data:
        moyennes.append(moyenne_module(Data, module))
    moyenne_generale = sum(moyennes) / len(moyennes)
    return moyenne_generale


#6. Pour retourner True si le stagiaire obtient une moyenne générale >= 10 et False sinon :

def validation_moyenne_generale(Data):
    moyenne_generale = moyenne_generale(Data)
    if moyenne_generale >= 10:
        return True
    else:
        return False


#7. Pour saisir les notes de 5 modules et les ajouter au dictionnaire Data en utilisant la fonction de la question 1 et traiter ces notes en utilisant les autres fonctions ci-dessus :

Data = {}
for i in range(5):
    module = input("Entrez le nom du module : ")
    notes = []
    for j in range(3):
        note = int(input("Entrez la note : "))
        notes.append(note)
    Data = ajouter_notes(Data, module, notes)

module_plus_elevee = module_moyenne_plus_elevee(Data)
module_plus_faible = module_moyenne_plus_faible(Data)
moyenne_generale = moyenne_generale(Data)
validation_moyenne_generale = validation_moyenne_generale(Data)

print("Le module avec la moyenne la plus élevée est :", module_plus_elevee)
print("Le module avec la moyenne la plus faible est :", module_plus_faible)
print("La moyenne générale est :", moyenne_generale)
if validation_moyenne_generale:
    print("Le stagiaire a obtenu une moyenne générale >= 10")
else:
    print("Le stagiaire a obtenu une moyenne générale < 10")


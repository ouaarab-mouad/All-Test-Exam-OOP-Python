class FormationError(Exception):
    def __init__(self,message,code_erreur):
        self.message = message
        self.code_erreur = code_erreur

    def __str__(self):
        return f'une Erreur est survenue{self.message}:code_erreur:{self.code_erreur}'

class NiveauInvalideError(FormationError):
    def __init__(self,message,code_erreur,niveau):
        super().__init__(message,code_erreur)
        self.niveau = niveau

class PrerequisNonRespecteError(FormationError):
    def __init__(self,message,code_erreur,prerequis):
        super().__init__(message,code_erreur)
        self.prerequis = prerequis


try:
    # Inscription à une formation
    niveau = "expert"
    prerequis = ["Python"]
    # Vérification du niveau
    if niveau not in ["debutant", "intermediaire", "avance"]:
        raise NiveauInvalideError("Niveau de formation invalide",100,niveau)
    # Vérification des prérequis
    if niveau == "avance" and "Python" not in prerequis:
        raise PrerequisNonRespecteError("Les prérequis ne sont pas respectés",200,prerequis)
    # Inscription réussie
    print("Inscription réussie !")
except FormationError as e:
    print(e)

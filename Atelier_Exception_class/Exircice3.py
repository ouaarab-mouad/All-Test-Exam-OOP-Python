class FormationError(Exception):
    def __init__(self, message, code_erreur):
        self.message = message
        self.code_erreur = code_erreur

        super().__init__(self.message)
class NiveauInvalideError(FormationError):
    def __init__(self, message, niveau, code_erreur):
        self.niveau = niveau
        super().__init__(message, code_erreur)

    def __str__(self):
        return f"NiveauInvalideError: {self.message} ({self.code_erreur}) - Le niveau {self.niveau} est invalide."
class PrerequisNonRespecteError(FormationError):
    def __init__(self, message, niveau, code_erreur):
        self.niveau = niveau
        self.prerequis = prerequis
        super().__init__(message, code_erreur)

    def __str__(self):
        return f"PrerequisNonRespecteError: {self.message} ({self.code_erreur}) - Les prérequis suivants sont obligatoires pour le niveau {self.niveau}: {self.prerequis}."


try:
 # Inscription à une formation
    
    niveau = "avance"
    prerequis = ["Python"]

 # Vérification du niveau
    
    if niveau not in ["debutant", "intermediaire", "avance"]:
        raise NiveauInvalideError("Niveau de formation invalide")
    
 # Vérification des prérequis
    
    if niveau == "avance" and "Python" not in prerequis:
        raise PrerequisNonRespecteError("Les prérequis ne sont pas respectés", niveau, 102)
    
 # Inscription réussie
    
    print("Inscription réussie !")
except FormationError as e:
 print(f"Erreur : {e.message} (code {e.code_erreur})")
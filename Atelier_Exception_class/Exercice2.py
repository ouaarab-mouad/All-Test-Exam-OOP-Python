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
        return f"NiveauInvalideError: {self.message} {self.code_erreur} - Le niveau {self.niveau} est invalide."
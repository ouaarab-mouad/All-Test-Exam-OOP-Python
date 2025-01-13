class FormationError(Exception):
    def __init__(self, message, code_erreur):
        self.message = message
        self.code_erreur = code_erreur

        super().__init__(self.message)

class Shiritori:
    def __init__(self):
        self.words = []  # liste de mots déjà prononcés
        self.game_over = False  # jeu en cours

    def play(self, word):
        if not self.game_over:
            if len(self.words) == 0 or (word not in self.words and word[0] == self.words[-1][-1]):
                self.words.append(word)
                return self.words
            else:
                self.game_over = True
                return "game over"
        else:
            return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "jeu redémarré"


# Exemple d'utilisation de la classe Shiritori
shiritori_game = Shiritori()

print(shiritori_game.play("chat"))  # ['chat']
print(shiritori_game.play("tomate"))  # ['chat', 'tomate']
print(shiritori_game.play("éléphant"))  # game over
print(shiritori_game.play("table"))  # game over

print(shiritori_game.words)  # ['chat', 'tomate']
print(shiritori_game.restart())  # jeu redémarré
print(shiritori_game.words)  # []
print(shiritori_game.game_over)  # False

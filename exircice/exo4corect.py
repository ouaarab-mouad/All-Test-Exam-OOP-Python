class Shistori:
    def __init__(self):
        self.words=[]
        self.gme_over=False
    def play(self,word):
        #verevication de la prmiere regle et le deuxiem regles
        if not self.words:
            self.words.appendA(word)
        elif word[0]==self.words[-1][-1] and word not in self.words:
            self.words.append(word)






shiritori_game = Shistori()

print(shiritori_game.play("chat"))  # ['chat']
print(shiritori_game.play("tomate"))  # ['chat', 'tomate']
print(shiritori_game.play("éléphant"))  # game over
print(shiritori_game.play("table"))  # game over

print(shiritori_game.words)  # ['chat', 'tomate']
print(shiritori_game.restart())  # jeu redémarré
print(shiritori_game.words)  # []
print(shiritori_game.game_over)  # False

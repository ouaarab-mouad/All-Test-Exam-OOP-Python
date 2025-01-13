class Conway:
    def __init__(self):
        self.previous_term = "1"

    def __iter__(self):
        return self

    def __next__(self):
        current_term = self.previous_term
        self.previous_term = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(self.previous_term)])
        return current_term

import itertools

# Exemple d'utilisation
conway_iter = Conway()
for _ in range(7):
    print(next(conway_iter))

#Approche procédurale avec yield

def conway():
    term = "1"
    while True:
        yield term
        term = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(term)])

# Exemple d'utilisation
conway_gen = conway()
for _ in range(7):
    print(next(conway_gen))

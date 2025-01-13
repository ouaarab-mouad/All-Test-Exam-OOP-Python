class MultiplesDeN:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n**2:
            multiple = self.current
            self.current += self.n
            return multiple
        else:
            raise StopIteration

# Exemple d'utilisation
iterateur = MultiplesDeN(5)
for multiple in iterateur:
    print(multiple, end=" ")
print()

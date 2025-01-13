class MultiplesIterator:
    def __init__(self, N):
        self.N = N
        self.current = N

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.N**2:
            multiple = self.current
            self.current += self.N
            return multiple
        else:
            raise StopIteration

# Exemple d'utilisation
N = 5
multiples_iter = MultiplesIterator(N)
for multiple in multiples_iter:
    print(multiple, end=" ")

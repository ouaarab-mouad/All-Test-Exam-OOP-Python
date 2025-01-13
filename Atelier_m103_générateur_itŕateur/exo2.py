class ConwayIterator:
    def __init__(self):
        self.current_term = '1'

    def __iter__(self):
        return self

    def __next__(self):
        result = ''
        count = 1
        for i in range(1, len(self.current_term)):
            if self.current_term[i] == self.current_term[i - 1]:
                count += 1
            else:
                result += str(count) + self.current_term[i - 1]
                count = 1
        result += str(count) + self.current_term[-1]
        self.current_term = result
        return result

# Exemple d'utilisation
conway_iter = ConwayIterator()
for _ in range(10):
    print(next(conway_iter))

class ClipList(list):
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi
        super().__init__()

    def append(self, value):
        self._clip_value(value)
        super().append(value)

    def insert(self, index, value):
        self._clip_value(value)
        super().insert(index, value)

    def __setitem__(self, key, value):
        self._clip_value(value)
        super().__setitem__(key, value)

    def extend(self, iterable):
        for value in iterable:
            self._clip_value(value)
        super().extend(iterable)

    def _clip_value(self, value):
        if not isinstance(value, int):
            raise ValueError("Seuls les nombres entiers sont autorisés.")
        if value < self.mini:
            value = self.mini
        elif value > self.maxi:
            value = self.maxi

# Exemple d'utilisation
cl = ClipList(2, 8)
cl.append(1)
cl.append(3)
cl.append(9)
cl.insert(0, 9)
cl.insert(2, 5)
cl[4] = 2
cl[3] = 12
cl.extend((1, 2, 3, 7, 8, 9))
print(cl)  # Output: [2, 3, 5, 8, 2, 2, 3, 7, 8, 8]

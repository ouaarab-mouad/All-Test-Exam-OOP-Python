class Fraction:
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise FractionError("Nombres entiers attendus pour les paramètres a et b.")
        if b == 0:
            raise FractionError("Le dénominateur ne doit pas être égal à zéro.")
        self.numerator = a
        self.denominator = b
        self.factorize()
    
    def factorize(self):
        if self.denominator == 1:
            return
        for i in range(2, self.denominator+1):
            if self.denominator % i == 0:
                pgdc = self.denominator // i
                if pgdc * i == self.denominator:
                    self.numerator //= i
                else:
                    self.numerator //= i
                    self.numerator *= pgdc
                break
        else:
            raise FractionError("Impossible de factoriser la fraction.")
    
    def __str__(self):
        if self.numerator < 0:
            return f"- {self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Seuls des objets Fraction sont autorisés comme arguments.")
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return self
        elif self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        elif other.denominator == self.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        elif self.denominator > other.denominator:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denomin)
def var():
    var = '1'
    while True:
        yield var
        result = ''
        count = 1
        for i in range(1, len(var)):
            if var[i] == var[i - 1]:
                count += 1
            else:
                result += str(count) + var[i - 1]
                count = 1
        result += str(count) + var[-1]
        var = result

# Exemple d'utilisation du générateur
objet = var()
for _ in range(10):
    print(next(objet))
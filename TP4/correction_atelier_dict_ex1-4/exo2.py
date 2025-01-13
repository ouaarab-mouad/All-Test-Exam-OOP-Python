def addToDict(D,k,v):
    if k in D.keys():
        pass
    else:
        D[k]=v

    return D

D = {0: 10, 1: 20}
k = int(input('Saisir une clé:'))
v = int(input('saisir une valeur:'))
print(addToDict(D,k,v))

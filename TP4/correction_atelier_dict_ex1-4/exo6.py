def addNote(D,module,notes):
    D[module] = notes
    return D

def MoyModule(D,module):
    return sum(D[module])/len(D[module])

def maxMoy(D):
    max_moy = MoyModule(D,list(D.keys())[0])
    max_module = list(D.keys())[0]
    for module in D.keys():
        if MoyModule(D,module) > max_moy:
            max_moy = MoyModule(D,module)
            max_module = module

    return max_module

def minMoy(D):
    min_moy = MoyModule(D,list(D.keys())[0])
    min_module = list(D.keys())[0]
    for module in D.keys():
        if MoyModule(D,module) < min_moy:
            min_moy = MoyModule(D,module)
            min_module = module

    return min_module

def moyGen(D):
    S = 0
    for module in D.keys():
        S += MoyModule(D,module)

    return S/len(D.keys())

def isAdmis(D):
    return  moyGen(D)>=10

Data = [
('PSP', (10, 12, 11)),
 ('POOP', (14, 10, 8)),
 ('BDP', (9, 10, 14)),
 ('WEB', (12, 13, 10)),
 ('DATA', (13, 15, 17))
]
D = {}
for item in Data:
    addNote(D,item[0],item[1])

#1
print(D)

#2
print(f'la moyenne obtenue dans le module POOP:{MoyModule(D,"POOP")}')

#3
print(f'Le module avec la moyenne la plus élevée est:{maxMoy(D)}')
#4
print(f'Le module avec la moyenne la plus faible est :{minMoy(D)}')

#5
print(f'La moyenne générale obtenue par le stagiaire est:{moyGen(D)}')

#6
print(f'Décision : le stagiaire passe:{isAdmis(D)}')


dictionnaire = {1 : 2, 3 : 4, 4 : 3, 2 : 1, 0 : 0} 
print("Dictionnaire original :",dictionnaire)
sorder_dict = sorted(dictionnaire.items(),key=lambda x: x[1])
print("Dictionnaire par ordre croissant de valeur :",sorder_dict)
sorder_dict.reverse()
print("Dictionnaire par ordre décroissant de valeur :",sorder_dict)
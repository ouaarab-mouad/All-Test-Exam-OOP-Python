liste={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    
x=int(input("saisire le cle a recherch : "))
y=int(input("saisire la valeur a recherch : "))
print(x in liste.keys())
print(y in liste.values())

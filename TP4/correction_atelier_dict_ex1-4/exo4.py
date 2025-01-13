def keyInDict(D,k):
    return k in D.keys()

def valueInDict(D,v):
    return v in D.values()

D = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 99

print(keyInDict(D,key))
print(valueInDict(D,99))

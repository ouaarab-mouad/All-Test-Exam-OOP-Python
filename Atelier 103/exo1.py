stk=0
class Stack:
 def __init__(self):
    self.__stk = []
 def push(self, val):
    self.__stk.append(val)
 def pop(self):
    val = self.__stk[-1]
    del self.__stk[-1]
    return val
class CountingStack(Stack):
 def __init__(self):
 # Remplissez le constructeur avec les actions appropriées.
    def get_counter(self):
 # retourner la valeur du compteur pour une pile donnée
        def pop(self):
 # faire un pop() et incrémenter le compteur
 
         stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
    print(stk.get_counter())
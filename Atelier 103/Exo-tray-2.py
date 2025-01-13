class Queue:
 def __init__(self):
 #écrire votre code ici

    def put(self, elem):
 #écrire votre code ici
    def get(self):
 #écrire votre code ici
que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
 for i in range(4):
    print(que.get())
except:
    print("Queue error")
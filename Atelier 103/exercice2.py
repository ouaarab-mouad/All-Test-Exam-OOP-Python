class Queue:
    def __init__(self):
        self.__stk = []
    def put(self, elem):
        self.__stk.append(elem)
    def get(self):
        elem = self.__stk[0]
        del self.__stk[0]
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
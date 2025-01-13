class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.append(elem)

    def get(self):
        if not self.isEmpty():
            elem = self.__stk[0]
            del self.__stk[0]
            return elem
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.__stk) == 0


class SuperQueue(Queue):
    def isEmpty(self):
        return super().isempty()


# Example usage
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

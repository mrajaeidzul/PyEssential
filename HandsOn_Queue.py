class Queue:
    def __init__(self):
        self.__box = []
    def put(self, elem):
        self.__box.append(elem)
    def get(self):
        if len(self.__box) == 0:
            raise QueueError
        val = self.__box[-1]
        del self.__box[-1]
        return val

class QueueError(Exception):
    pass

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(i,"-",que.get())
except QueueError:
    print("Cannot get() new element. The Queue is empty")

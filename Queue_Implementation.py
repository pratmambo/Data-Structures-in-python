class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def showQueue(self):
        for item in self.items:
            print(item, end=" ")
        print()

    def size(self):
        return len(self.items)


k = Queue()
k.enqueue(6)
k.enqueue(3)
k.enqueue(4)
k.showQueue()
print(k.dequeue())
k.showQueue()
print(k.dequeue())
k.showQueue()
print(k.dequeue())
k.showQueue()
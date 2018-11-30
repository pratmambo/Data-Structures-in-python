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


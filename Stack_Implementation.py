class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def balance_check(s):
    stac = Stack()
    stac.push(s[0])
    for char in s[1:]:
        if stac.peak() == char:
            stac.pop

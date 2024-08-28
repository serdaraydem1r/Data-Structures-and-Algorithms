'''
Deque()
    addRight()
    addLeft()
    removeRight()
    removeLeft()
    isEmpty()
    size()
'''
class Deque():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addRight(self, item):
        self.items.append(item)
    def addLeft(self, item):
        self.items.insert(0, item)
    def removeRight(self):
        return self.items.pop()
    def removeLeft(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
deque = Deque()
deque.addRight(1)
deque.addRight(2)
deque.addLeft(3)
deque.addLeft(4)
print(deque.size())
print(deque.removeRight())
print(deque.removeLeft())
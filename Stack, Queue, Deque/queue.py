'''
Queue()
    enqueue(element)
    dequeue()
    size()
    isEmpty()
'''

class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, element):
        self.items.insert(0,element)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
myQueue = Queue()
print(myQueue.isEmpty())
myQueue.enqueue(5)
myQueue.enqueue(6)
myQueue.enqueue(7)
myQueue.enqueue(8)
print(myQueue.size())
print(myQueue.isEmpty())
print(myQueue.dequeue())
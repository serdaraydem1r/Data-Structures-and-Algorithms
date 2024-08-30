#Node -> Linked List

#Singly Linked List

class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
print(firstNode.nextNode.value) #20 birinci node üzerinde 2.node değerine ulaştık
print(firstNode.nextNode.nextNode.value) #30 birinci node üzerinden 3.node değerine ulaştık

#Doubly Linked List

class DoublyNode():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

firstNode = DoublyNode(10)
secondNode = DoublyNode(20)
thirdNode = DoublyNode(30)
firstNode.nextNode = secondNode
secondNode.prevNode = firstNode
secondNode.nextNode = thirdNode
thirdNode.prevNode = secondNode
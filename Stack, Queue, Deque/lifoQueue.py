from queue import LifoQueue # stack

lifoQueue = LifoQueue()
lifoQueue.put(1) # push
lifoQueue.put(2)
lifoQueue.put(3)
print(lifoQueue.get()) # pop, en son eklenen neyse onu çıkarıyor.

#%%
from queue import Queue

queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())

#%%
from collections import deque

deque = deque()
deque.append(1)
deque.append(2)
deque.append(3)
deque.appendleft(4)
deque.pop()
deque.popleft()
print(deque)
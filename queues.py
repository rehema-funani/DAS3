
#implementation using list
#Adding item in a list
queue = []
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
#Removing item from a queue
print(queue.pop())
print(queue)

#Implementation using deque
from collections import deque
#Adding items in a queue
myqueue = deque()
myqueue.append("Rahma")
myqueue.append("Adhan")
myqueue.append("Mansa")

print(myqueue)
print(myqueue.popleft())

#Implementation using queues
from queue import Queue
b = Queue(maxsize = 3)
print(b.put("shoes"))
print(b)



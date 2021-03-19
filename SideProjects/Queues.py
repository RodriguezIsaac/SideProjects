#Queues are very similar to lists with the difference being that queues have specific order of how elements get in & out

import queue

#todo Code for "first in first out" queue meaning the first element to enter the queue is the first to leave the queue
"""
#Creates a queue assigned to the variable q
q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]

#Places each number from the numbers list into the queue
for number in numbers:
    q.put(number)

#Retrieves the number from the queue
print(q.get())
print(q.get())
"""

#todo Code for "last in first out" queue (last element in is the first to leave)
'''
#Creates a Last in first out (Lifo) Queue
q = queue.LifoQueue()

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())
'''

#todo Code for Priority Queue
#Allows you to give every element a certain priority by passing a tuple
q = queue.PriorityQueue()

#Lower the priority number, the more priority the element has
#Note: q.put((2, "Hello World")) is treated as a list. 2 is place 0 while "Hello World" is place 1
q.put((2, "Hello World"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

#Loop that continues until the queue is empty
while not q.empty():
    print(q.get()[1])
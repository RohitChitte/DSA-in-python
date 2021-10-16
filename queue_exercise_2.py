from collections import deque
from time import sleep
import threading

class Queue:
    def __init__(self):
        self.buffer = deque() 

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return

        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def isempty(self):
        return len(self.buffer)==0

    def front(self):
        return self.buffer[-1]


q = Queue()

def enque_binary(num):
    q.enqueue(bin(1)[2:])
    for i in range(1,int(num+2)//2):
        number = str(bin(i)[2:])
        q.enqueue(number+'0')
        q.enqueue(number+'1')
    
    print("Printing binary numbers using queues ")
    i=0
    size = q.size()
    while i<=size-2:
        print(q.front())
        q.dequeue()
        i+=1

enque_binary(10)

# pls reffer to approach given in codebasics code for this exercise. 
# link --->  https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/Exercise/binary_numbers.py

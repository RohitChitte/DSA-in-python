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

q = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(orders):
    for i in orders:
        print("Placing order for item ",i)
        q.enqueue(i)
        sleep(0.5)
        

def serve_order():
    sleep(1)
    while not q.isempty():
        order = q.dequeue()
        print("Now serving order for ",order)
        sleep(2)
        

t1 = threading.Thread(target=place_order,args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()


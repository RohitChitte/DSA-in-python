from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque() 

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def isempty(self):
        return len(self.buffer)==0

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer,'\n')
pq.dequeue()
print(pq.buffer,'\n')
print(pq.size())
print(pq.isempty())
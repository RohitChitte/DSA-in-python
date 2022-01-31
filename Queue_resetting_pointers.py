# This class is implementation of circular queue datastructure for theory reffer abdul bari queue screenshots in google drive .

class Queue_array:
    def __init__(self,size):
        self.front = 0
        self.rear =  0
        self.size = size
        self.arr = [None for i in range(self.size)]

    def enqueue(self,data):
        if (self.rear+1)%self.size == self.front:
            print("Queue is full")
        else:
            self.rear = (self.rear+1)%self.size
            self.arr[self.rear] = data


    def dequeue(self):
        x = -1
        if self.front == self.rear:
            return "Queue is empty"
        else:
            self.front = (self.front+1)%self.size
            x = self.arr[self.front]
            self.arr[self.front] = None
        return x

    def display(self):
        print(self.arr)

    def isempty(self):
        if self.rear == self.front:
            return True
        else :
            return False

    def isFull(self):
        if self.rear == self.size -1 :
            return True
        else:
            return False

    def first(self):
        if self.front == None:
            return self.arr[0]
        return self.arr[self.front+1]

    def last(self):
        if self.rear == None:
            return "Empty queue"
        return self.arr[self.rear]


obj = Queue_array(9)
obj.display()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(21)
obj.enqueue(100)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(21)
obj.enqueue(100)
obj.display()
print(obj.dequeue())
obj.display()
obj.enqueue(6)
obj.display()
obj.dequeue()
obj.display()
obj.enqueue(7)
obj.display()
for i in range(7):
    print(obj.dequeue())

obj.display()




class Queue_array:
    def __init__(self,size):
        self.front = None
        self.rear =  None
        self.size = size
        self.arr = [None for i in range(self.size)]

    def enqueue(self,data):
        if self.rear == self.size-1:
            print("Queue is full")
        else:
            if self.rear == None:
                self.rear = 0
                self.arr[self.rear] = data
            else:
                self.rear += 1
                self.arr[self.rear] = data


    def dequeue(self):
        x = -1
        if self.front == self.rear:
            return "Queue is empty"
        else:
            if self.front == None:
                self.front = 0
                x = self.arr[self.front]
                self.arr[self.front] = None
            else:
                self.front += 1
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
obj.display()
print("First",obj.first())
print("Last",obj.last())
obj.dequeue()
obj.display()
obj.dequeue()
obj.display()




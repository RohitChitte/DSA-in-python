class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


class Queue_Linked_list:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        node = Node(data,None)
        if node == None:
            print("Queue is full ")
        elif self.front == None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deque(self):
        x = -1
        if self.front == None:
            return "Queue is empty"
        else:
            x = self.front.data
            self.front = self.front.next
        return x

    def display(self):
        itr = self.front
        while itr:
            print(itr.data,end = "")
            if itr.next:
                print("---->",end = "")
            itr = itr.next
        print()

    def isfull(self):
        node = Node()
        if node == None:
            return True
        else:
            return False
    def first(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.front.data

    def last(self):
        if self.rear == None:
            return "Queue is Empty"
        else:
            return self.rear.data

obj = Queue_Linked_list()
obj.enqueue(21)
obj.enqueue(3)
obj.enqueue(30)
obj.enqueue(210)
obj.display()
print(obj.deque())
obj.display()
print(obj.first())
print(obj.last())
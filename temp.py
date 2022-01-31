"""

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def Print(self):
        if self.head == None:
            print("Empty Linked list")
            return
        else:
            itr = self.head
            while itr:
                print(itr.data,end="")
                if itr.next:
                    print("--->",end="")
                itr = itr.next
            print()
            return ll

    def insert_at_end(self,data):
        if self.head == None :
            self.head = Node(data,None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def insert_at(self,index,data):
        if index == 0 :
            self.head = Node(data,self.head.next)


        else:
            if index >= 0 and index < self.get_length():
                itr = self.head
                count = 0
                while itr:
                    if count == index -1:
                        break
                    count += 1
                    itr = itr.next
                node = Node(data,itr.next)
                itr.next = node

    def remove_at(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            if index >= 0 and index < self.get_length():
                itr = self.head
                count = 0
                while itr:
                    if count == index -1 :
                        break
                    itr = itr.next
                    count += 1
                itr.next = itr.next.next
    def insert_value(self,lst):
        self.head = None
        self.head = Node(lst[0],None)
        itr = self.head
        for i in range(1,len(lst)):
            node = Node(lst[i],None)
            itr.next = node
            itr = itr.next




ll = Linked_List()
ll.insert_at_begining(2)
ll.insert_at_begining(23)
ll.insert_at_begining(5)
ll.insert_at_begining(31)
ll.Print()
ll.insert_at_end(56)
ll.insert_at(3,21)
ll.insert_at(0,100)
ll.Print()
ll.remove_at(3)
ll.Print()
ll.remove_at(0)
ll.Print()
ll.insert_value([1,2,3,4,5,6])
ll.Print()
#print(ll.get_length())

"""
"""
class hash_table:
    def __init__(self,max):
        self.max = max
        self.arr = [None for i in range(max)]

    def hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h%self.max

    def add(self,key,value):
        h = self.hash(key)
        self.arr[h] = value

ht = hash_table(10)
print(ht.arr,ht.max)
print(ht.hash('Rohit'))
ht.add('Rohit','Chitte')
print(ht.arr,ht.max)
"""

print(*range(5))
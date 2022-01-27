from collections import deque


class stack:
    from collections import deque
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self,position):
        if position<=self.size():
            return self.container[-position]

    def stackTop(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isempty(self):
        return len(self.container)==0

    def display(self):
        for i in range(self.size()-1,-1,-1):
            print(self.container[i])



s = stack()
s.push(3)
s.push(4)
s.push(5)
s.push(8)
print("Peek Operation ",s.peek(1))
print("Printing the Stack")
s.display()
print("\nPop Operation",s.pop())
print("Size",s.size())
print("object",s.container)
print("Empty status",s.isempty())
print("stack top",s.stackTop())


def reversestring(value):
    s = stack()
    string = ""
    for char in value:
        s.push(char)
    for i in range(len(value)):
        string += s.pop()
    return string 

#print(reversestring("We will conquere COVID-19"))

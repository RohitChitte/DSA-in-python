from collections import deque


class stack:
    from collections import deque
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isempty(self):
        return len(self.container)==0

"""
s = stack()
s.push(3)
print(s.peek())
s.push(4)
print(s.size())
s.pop()
print(s.size())
print(s.peek())
print(s.container)
print(s.isempty())
"""

def reversestring(value):
    s = stack()
    string = ""
    for char in value:
        s.push(char)
    for i in range(len(value)):
        string += s.pop()
    return string 

print(reversestring("We will conquere COVID-19"))

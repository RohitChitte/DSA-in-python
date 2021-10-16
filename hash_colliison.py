class hash_tables:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr=[[] for i in range(self.MAX)]

    def hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self,key,value):
        h = self.hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx]=(key,value)
                found = True
                break
        if not found:
            self.arr[h].append([key,value])

    def __getitem__(self,key):
        h = self.hash(key)
        for element in (self.arr[h]):
            if element[0]==key:
                return element[1]        
                #return element

    def __delitem__(self,key):
        h = self.hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] ==  key:
                del self.arr[h][idx]



a = hash_tables(50)
a["march 6"]=123
a["march 6"]=78
a["march 17"]=88
print(a["march 17"])
print(a.arr)
del a["march 17"]
print(a.arr)
del a["march 6"]
print(a.arr)
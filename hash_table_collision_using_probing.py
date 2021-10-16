class hash_tables:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr=[None for i in range(self.MAX)]

    def hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self,key,value):
        h = self.hash(key)
        if self.arr[h] is None:
            self.arr[h]=(key,value)
        else :
            for i in range(self.MAX):
                if self.arr[i] is None:
                    self.arr[i]=value
                    h = 


    def __getitem__(self,key):
        h = self.hash(key)
        self.arr[]       
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
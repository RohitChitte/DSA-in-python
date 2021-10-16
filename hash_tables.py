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
        self.arr[h]=value

    def __getitem__(self,key):
        h = self.hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.hash(key)
        self.arr[h]=None


h = hash_tables(20)
print(h.hash("march 6"))
h["march 6"] = 210
print(h["marhc 6"])
del(h["march 6"])
print(h["march 6"])
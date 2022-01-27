

# This Class is Hash Table Implementation using Quadratic Probing technique .

class hash_tables:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr=[None for i in range(self.MAX)]

    def hash(self,key):  #This is hash funciton it takes in the key itereate over the characters and add their asci values and takt the unit value of sum of ascii values.
        """
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX
        """
        index = key % self.MAX
        if self.arr[index] == None :
            return index
        else:
            i = 1
            while (self.arr[(index+(i**2))%self.MAX]!=None) :
                i = i+1
            return (index+(i**2))%self.MAX

    def insert(self,key):
        h = self.hash(key)
        self.arr[h] = key

    def search(self,key):
        h = key % self.MAX
        i = 0
        if self.arr[h]!= key:
            while ((self.arr[(h+(i*i))%self.MAX]!=key) and self.arr[(h+(i*i))%self.MAX]!=None):
                i = i+1
        if (self.arr[(h+(i**2))%self.MAX])==key:
            return (h+(i**2))%self.MAX
        else:
            return None

    def __delitem__(self,key):
        h = self.hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] ==  key:
                del self.arr[h][idx]

    def display_Hash_Table(self):
        for i in range(self.MAX):
            print(i,end = " ")
            for j in self.arr[i]:
                print("---->"+j[1],end = " ")
            print()


hh = hash_tables(10)
hh.insert(23)
print(hh.arr)
hh.insert(13)
hh.insert(33)
print(hh.arr)
print(hh.search(23))
print(hh.search(13))
print(hh.search(33))
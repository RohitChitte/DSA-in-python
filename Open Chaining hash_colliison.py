
# Below code is for Hash collision techniqye (Open chaining) .

class hash_tables:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr=[[] for i in range(self.MAX)]

    def hash(self,key):  #This is hash funciton it takes in the key itereate over the characters and add their asci values and takt the unit value of sum of ascii values.
        """
        h = 0
        for char in key:
            h+=ord(char)
        return h%self.MAX
        """
        return key%self.MAX
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

    def display_Hash_Table(self):
        for i in range(self.MAX):
            print(i,end = " ")
            for j in self.arr[i]:
                print("---->"+j[1],end = " ")
            print()



a = hash_tables(10)
a[10] = "Rohit"
a[20] =  "Chitte"
a[56] = "kolhe"
a[16] = "Nana"
#print(a.arr)
a.display_Hash_Table()
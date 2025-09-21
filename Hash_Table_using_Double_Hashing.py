class hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hash_(self,key):
        return (hash(key)%self.size)
    def insert(self,key,value):
        index=self.hash_(key)
        if(self.table[index]==None):#if the slot is empty then proceed to place the element in the hash table
            self.table[index]=(key,value)
        else:#collision occurs!
            i=1
            h2=1+(self.hash_(key)%(self.size-1))
            new_index=(index+i*h2)%self.size
            while(self.table[new_index]!=None and i<self.size):
                i+=1
                new_index = (index + i * h2) % self.size
            if(self.table[new_index]==None):
                self.table[new_index]=(key,value)
            else:
                print('Hash Table Full Bro!')
    def display(self):
        for i in range(self.size):
            print(f'{i}:{self.table[i]}')
ht=hashtable(5)
ht.insert(12,2)
ht.insert(2,4)
ht.insert(19,6)
ht.insert(23,3)
ht.display()
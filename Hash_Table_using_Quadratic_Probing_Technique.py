class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def __hash__(self,key):
        return(hash(key)%self.size)
    def insert(self,key,value):
        index=self.__hash__(key)
        if(self.table[index]==None):#if this place empty you can place the key-value here
            self.table[index]=(key,value)
        else:#collision occured we are using Quadratic probing
            print('Collision Occurs!')
            i=1
            original_index=(index+i**2)%self.size
            while(self.table[original_index]!=None and i<(self.size)):#i am iterating until i found the next avilable slot
                i+=1
                original_index=(index+i**2)%self.size
            if(self.table[original_index]==None):
                self.table[original_index]=(key,value)
            else:
                print('Hash table is full')
    def display(self):
        for i in range(self.size):
            print(f'{i}:{self.table[i]}')
ht=HashTable(3)
ht.insert(12,2)
ht.insert(2,4)
ht.insert(19,6)
ht.insert(23,3)
ht.display()
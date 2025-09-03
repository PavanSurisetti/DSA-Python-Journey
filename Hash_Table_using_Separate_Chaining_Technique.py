class node:
    def __init__(self,key,value):
        self.key=key 
        self.value=value 
        self.next=None
#node will create successfully 
class hashTable:
    def __init__(self,size):
        self.size=size
        self.no_of_elements=0
        self.table=[None]*self.size
    def __hash__(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index=self.__hash__(key)#function call
        if(self.table[index] is None):#checking whether the  slot is empty or not
            self.table[index]=node(key,value)#if it is empty then we will assign the value to the index returned by the hash function
            self.no_of_elements+=1
        else:#if collision occurs
            temp=self.table[index]#it will return the address of the node.
            while temp :
                if(temp.key==key): #if the key already exists, then it will update with the new value  
                    temp.value=value#here i am updating the value
                    return
                temp=temp.next#updating  a location
            new_node=node(key,value)
            new_node.next=self.table[index]#here i am assigning the node at the first position
            self.table[index]=new_node
            self.no_of_elements+=1
    def delete(self,key):
        index=self.__hash__(key)
        temp=self.table[index]#assiging to  a temp variable
        prev=None#prev keeps track of the node before temp.
        while temp:
            if(temp.key==key):
                if(prev):
                    prev.next=temp.next
                else:
                    self.table[index]=temp.next
                self.no_of_elements-=1
                return 
            prev=temp 
            temp=temp.next
    def display(self):
        for i in range(self.size):
            print(f'Index:{i}')
            temp=self.table[i]
            if(temp is not None):
                while(temp):
                    print(f'{temp.key}:{temp.value} ->',end=' ')
                    temp=temp.next
                print('None')
            else:
                print('Empty')
    def search(self,key):
        index=self.__hash__(key)
        temp=self.table[index]
        while temp:
            if(temp.key==key):
                return temp.value
            temp=temp.next
        return f'not there'
h=hashTable(10)
h.insert('A',12)
h.insert('B',13)
h.insert('C',12)
h.display()
print('===='*10)
h.delete('A')
h.display()
print(h.search('A'))
print(h.search('C'))
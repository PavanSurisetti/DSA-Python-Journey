#circular_single_linked_list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular_linked_list:#linked list class
    def __init__(self):#creating of head
        self.head=None
    def insertion_at_begin(self,data):
        new_node=node(data)
        if(self.head==None):#initially no nodes there,after the newnode assignig the address of newnode to its reference
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head#linking the last node address with first node address
            a=self.head
            while a.next is not self.head:#moving to the last position
                a=a.next
            a.next=new_node
            self.head=new_node
    def insertion_at_end(self,data):
        new_node=node(data)
        if(self.head==None):#if no nodes initially 
            self.head=new_node
            new_node.next=self.head
        else:#if more than one node  
            a=self.head
            while a.next is not self.head:#moving to the last position
                a=a.next#here in loop we have to check for location,so we should take the a.next in condition
            a.next=new_node
            new_node.next=self.head
    def insertion_at_random(self,data):
        new_node=node(data)
        position=int(input("Enter a Position:"))
        if(self.head==None):
            self.head=new_node
            new_node.next=self.head
        else:
            if(position==1):
                a=self.head
                while a.next is not self.head:
                    a=a.next
                new_node.next=self.head#here first you have to assign newnode address to head address
                self.head=new_node#making newnode as first node
                a.next=self.head#changing address of last node...
            else:
                a=self.head#for traversing purpose
                for i in range(1,position-1):
                    a=a.next
                new_node.next=a.next
                a.next=new_node 
    def deletion_at_begin(self):
        if(self.head==None):
            print('LinkedList is Empty')
        else:
            if(self.head.next==self.head):
                self.head=None
            else:
                a=self.head
                while a.next is not self.head:
                    a=a.next
                self.head=self.head.next #moving head to right side one position
                a.next=self.head
    def deletion_at_end(self):
        if(self.head==None):
            print('LinkedList is Empty')
        else:
            if(self.head.next==self.head):#if only one node
                self.head=None
            else: 
                a=self.head
                while a.next is not self.head:#moving to the end
                    a1=a
                    a=a.next#updating location
                a1.next=a.next# here i am assgining the last node address to the previous node address...
    def deletion_at_random(self):
        position=int(input("Enter a Position to Delete:"))
        if(self.head==None):
            print('LinkedList is Empty')
        else:
            if(position==1):#if position is 1
                if(self.head.next==self.head):#if it contains only one node 
                    self.head=None
                else:
                    a=self.head
                    while a.next is not self.head:
                        a=a.next
                    self.head=self.head.next #moving head to right side one position
                    a.next=self.head
            else:
                a=self.head
                for i in range(1,position-1):
                    a=a.next
                a.next=a.next.next
    def traversal(self):
        if(self.head==None):
            print("Empty LinkedList")
        else:
            a=self.head
            while True:
                print(a.data,'',end='')
                a=a.next#moving to the next location
                if(a==self.head):
                    break
        print()
cll=Circular_linked_list()
cll.insertion_at_begin(1)
cll.insertion_at_end(2)
cll.insertion_at_random(3)
cll.traversal()
cll.deletion_at_begin()
cll.deletion_at_random()
cll.deletion_at_end()
cll.traversal()

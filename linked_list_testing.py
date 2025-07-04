#linked_list_testing.py
class node:
    def __init__(self,data):
        self.data=data#data part
        self.next=None#address part
class SLL:
    def __init__(self):
        self.head=None
    def insertion_at_beginning(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def insertion_at_end(self,data):
        new_node=node(data)
        if(self.head is None):#is or == we can use both
           self.head= new_node
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            a.next=new_node
    def deletion_at_begin(self):
        if(self.head is None):
            print('Linked List is empty')
        else:
            a=self.head
            if(self.head.next==None):
                self.head=None
            else:
                self.head=self.head.next
                a.next=None
    def path(self):
        a=self.head
        while a  is not None:
            print(a.data,end=' ')
            a=a.next
        print()
sll=SLL()
sll.insertion_at_beginning(10)
sll.path()
sll.insertion_at_beginning(20)
sll.path()
sll.insertion_at_beginning(30)
sll.path()
print('------'*10)
sll.insertion_at_end(5)
sll.path()
sll.insertion_at_end(0)
sll.path()
print('------'*10)
sll.deletion_at_begin()
sll.path()
sll.deletion_at_begin()
sll.path()
#single_linked_list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single_linked_list:
    def __init__(self):
        self.head=None
    def insertion_at_begin(self,data):
        new_node=node(data)
        new_node.next=self.head#works even for the head is none
        self.head=new_node
    def insertion_at_end(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            a.next=new_node
    def insertion_at_random_position(self,data):
        new_node=node(data)
        position=int(input("Enter which Position to be inserted:"))
        a=self.head
        if(self.head==None):
            self.head=new_node
        else:
            if(position==1):
                new_node.next=self.head
                self.head=new_node
            else:
                for i in range(1,position-1):
                    a=a.next
                new_node.next=a.next
                a.next=new_node
    def deletion_at_begin(self):
        if(self.head==None):
            print("Linked List Empty")
        else:
            a=self.head
            if(self.head.next==None):
                self.head=None
            else:
                self.head=a.next
                a.next=None
    def deletion_at_end(self):
        if(self.head==None):
            print("Linked List Empty")
        else:
            if(self.head.next==None):
                self.head=None
            else:
                a=self.head.next
                prev_node=self.head
                while a.next is not None:
                    a=a.next
                    prev_node=prev_node.next
                prev_node.next=None
    def deletion_at_random_position(self):
        if(self.head==None):
            print('Linked List Empty')
        else:
            if(self.head.next==None):
                self.head=None
            else:
                position=int(input('Enter which position do you want to delete:'))
                if(position==1):#deleting the node at first node
                    temp=self.head
                    self.head=temp.next
                    temp.next=None
                else:
                    prev=self.head
                    a=self.head.next
                    for i in range(1,position-1):
                        a=a.next
                        prev=prev.next
                    prev.next=a.next
                    a.next=None
    def traversal(self):
        a=self.head
        while a is not None:
            print(a.data,end=' ')
            a=a.next
        print()
sll=Single_linked_list()
sll.insertion_at_begin(4)
sll.insertion_at_end(3)
sll.insertion_at_random_position(5)
sll.traversal()
sll.deletion_at_begin()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.insertion_at_begin(1)
sll.traversal()
sll.deletion_at_random_position()
sll.traversal()
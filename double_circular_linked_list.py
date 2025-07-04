#double_circular_linked_list.py
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class double_circular_linked_list:
    def __init__(self):
        self.head=None
    def insertion_at_begin(self,data):
        new_node=node(data)
        if(self.head==None):
                self.head=new_node
                new_node.next=self.head
                new_node.prev=self.head
                self.head=new_node
        else:
            tail=self.head.prev
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=tail
            tail.next=new_node
            self.head=new_node
    def insertion_at_end(self,data):
        new_node=node(data)
        if(self.head is None):
            self.head=new_node
            self.head.next=new_node
            self.head.prev=new_node
        else:
            a=self.head#temp variable
            while a.next is not self.head:
                a=a.next
            a.next=new_node
            new_node.prev=a
            new_node.next=self.head
            self.head.prev=new_node
    def insertion_at_random_position(self,data):
        new_node=node(data)
        position=int(input("Enter a Random Position to insert:"))
        if(self.head is None):
            self.head=new_node
            new_node.next=self.head
            new_node.prev=self.head
        elif(position==1):
            tail=self.head.prev
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=tail
            tail.next=new_node
            self.head=new_node
        else:
            a=self.head #temporary variable for storing  purpose
            for i in range(1,position-1):
                a=a.next
                if(a is self.head):
                    print('out of bounds')
                    return# to exit from the fucntion
            new_node.next=a.next
            a.next=new_node
            new_node.prev=a
            new_node.next.prev=new_node
    def deletion_at_begin(self):
        print('---deleting at begin---')
        if(self.head==None):
            print('Linked List is empty')
        else:
            if(self.head==self.head.next):
                self.head.prev=None
                self.head.next=None
            else:
                a=self.head
                tail=a.prev
                self.head=a.next#moving forward one step
                self.head.prev=tail
                tail.next=self.head
                a.next=a.prev=None
    def deletion_at_end(self):
        print('---deleting at end---')
        if(self.head==None):
            print('Linked List is empty')
        else:
            if(self.head==self.head.next):
                self.head.prev=None
                self.head.next=None
            else:
                a=self.head
                while a.next is not self.head:
                    temp=a
                    a=a.next
                temp.next=self.head
                self.head.prev=temp
                a.next=a.prev=None
    def deletion_at_random_position(self):
        print('---deleting at Random Position---')
        position=int(input('Enter a Position:'))
        if(self.head==None):
            print('Linked List is empty')
        else:
            if(self.head==self.head.next):
                self.head.prev=None
                self.head.next=None
            elif(position==1):
                a=self.head
                tail=a.prev
                self.head=a.next#moving forward one step
                self.head.prev=tail
                tail.next=self.head
                a.next=a.prev=None
            else:
                a=self.head
                for i in range(1,position-1):
                    a=a.next
                    if(a.next is self.head):
                        print('out of bounds')
                        return
                temp=a.next
                a.next=temp.next
                temp.next.prev=a
                temp.prev=temp.next=None

    def traversal(self):
        a=self.head
        while True:
            print(a.data,end='  ')
            a=a.next
            if(a ==self.head):
                break
        print()
cdll=double_circular_linked_list()
cdll.insertion_at_begin(10)
cdll.traversal()
cdll.insertion_at_begin(20)
cdll.traversal()
cdll.insertion_at_begin(30)
cdll.traversal()
cdll.insertion_at_begin(40)
cdll.traversal()
cdll.insertion_at_end(5)
cdll.traversal()
cdll.insertion_at_end(0)
cdll.traversal()
cdll.insertion_at_end(-5)
cdll.traversal()
cdll.insertion_at_random_position(100)
cdll.traversal()
cdll.deletion_at_begin()
cdll.traversal()
cdll.deletion_at_begin()
cdll.traversal()
cdll.deletion_at_end()
cdll.traversal()
cdll.deletion_at_end()
cdll.traversal()
cdll.deletion_at_random_position()
cdll.traversal()
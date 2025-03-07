#double_linked_list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class double_linked_list:
    def __init__(self):
        self.head=None
    def insertion_at_begin(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
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
            new_node.prev=a
    def insertion_at_random_position(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
        else:
            position=int(input('enter position to insert:'))
            if(position==1):
                new_node.next=self.head#you can use the insert at begin logic here        
                self.head.prev=new_node
                self.head=new_node
            else:
                a=self.head
                for i in range(1,position-1):
                    a=a.next
                new_node.next=a.next
                new_node.prev=a
                a.next=new_node
    def deletion_at_begin(self):
        if(self.head==None):
            print("Linked List Empty")
        else:
            if(self.head.next==None):#if only one node to handle that this will replace that
                self.head=None
            else:
                a=self.head
                self.head=a.next
                self.head.prev=None
                a.next=None
    def deletion_at_end(self):
        if(self.head==None):
            print("Linked List Empty")
        else:
            if(self.head.next==None):#if only one node to handle that this will replace that
                self.head=None
            else:
                a=self.head
                while a.next is not None:
                    a=a.next
                a.prev.next=None
                a.prev=None
    def deletion_at_random_position(self):
        if(self.head==None):
            print("linked list is empty")
        else:
                a=self.head
                position=int(input('Enter which postion to delete:'))
                if(position==1):
                    self.head=a.next
                    self.head.prev=None
                    a.next=None
                else:
                    for i in range(1,position-1):
                        a=a.next
                    temp=a.next
                    a.next=temp.next
                    if temp.next is not None:
                       temp.next.prev=a
                    temp.next=temp.prev=None
    def traversal(self):
        a=self.head
        if(a==None):
            print("Linked list empty")
        else:
            while  a is not None:
                print(a.data,end=' ')
                a=a.next
        print()
dll=double_linked_list()
dll.insertion_at_begin(3)
dll.traversal()
dll.insertion_at_begin(2)
dll.traversal()
dll.insertion_at_end(4)
dll.traversal()
dll.insertion_at_random_position(5)
dll.traversal()
dll.insertion_at_random_position(1)
dll.traversal()
dll.deletion_at_begin()
dll.traversal()
dll.deletion_at_end()
dll.traversal()
dll.deletion_at_random_position()
dll.traversal()
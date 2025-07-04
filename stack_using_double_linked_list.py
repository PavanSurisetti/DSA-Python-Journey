class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)#creating a node 
        if(self.head is None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        #here also i am using the begin for pushing the elements because it takes the less time when compared to the last insert or end insert
    def pop(self):
        if(self.head is None):
            print('stack underflow')
        else:
            a=self.head
            self.head=a.next
            if self.head:# this is to avoid error while deleting the last node so we use the if condition to check 
                self.head.prev=None
            a.next=None
    def traversal(self):
        if(self.head is None ):
            print('stack is empty')
        else:
            a=self.head
            while True:
                print(a.data)
                a=a.next
                if( a is None):
                    break
            print('===='*10)
s=stack()
s.push(3)
s.push(2)
s.push(1)
s.traversal()
s.pop()
s.traversal()
s.pop()
s.traversal()
s.pop()
s.traversal()
s.pop()
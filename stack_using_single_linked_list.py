class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)
        if(self.head is None):#for first element 
            self.head=new_node
        else:#more than one element
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if(self.head is None):
            print('Stack Underflow')
        else:
            a=self.head#here we used both begin only for pushing and popping 
            self.head=a.next
            a.next=None
    def traversal(self):
        a=self.head
        if(self.head is None):
            print('Stack is empty')
        else:
            while True:#if last location None we can traversing
                print(a.data)
                a=a.next#moving to next location
                if(a==None):
                    break
            print('==='*10)
s=stack()
s.push(1)
s.traversal()
s.push(2)
s.traversal()
s.push(3)
s.traversal()
s.push(4)
s.traversal()
s.push(5)
s.traversal()
s.pop()
s.traversal()
s.pop()
s.traversal()
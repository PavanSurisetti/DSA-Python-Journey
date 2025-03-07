#linked_list_testing
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single_linked_list:
    def __init__(self):
        self.head=None
    def traversal(self):
        a=self.head
        while a!=None:
            print(a.data,end=' ')
            a=a.next
sll=single_linked_list()
n1=node(5)
sll.head=n1
n2=node(4)
n1.next=n2
n3=node(3)
n2.next=n3
sll.traversal()
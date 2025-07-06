class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class queue:
    def  __init__(self):
        self.head=None  
    def enqueue(self,data):
        new_node=node(data)
        if(self.head is None):
            self.head=new_node
        else:
            a=self.head
            # here we will use insert at the end while inserting into the queue
            while a.next is not None:
                a=a.next
            a.next=new_node
            new_node.prev=a
    def dequeue(self):
        if(self.head is None):
            print('Hey the queue is Empty')
        else:
            if(self.head.next is None):
                print(f'{self.head.data} Deleted successfully!')
                self.head=None
            else:
                a=self.head
                self.head=a.next
                a.next=None
                self.head.prev=None
                print(f'{a.data} is deleted successfully!')
    def peek(self):
        if(self.head is None):
            print('The queue is empty')
        else:
             print(f'{self.head.data} is the peek element')
    def display(self):
        if(self.head is None):
            print('Hey Queue is Empty')
        else:
            a=self.head
            print('==='*5)
            while a is not None:#i have move upto the last location
                print(a.data,end=' ')
                a=a.next
            print()
            print('==='*5)
q=queue()
while(1):
    print('\nQueue Operations:\n1. Enqueue\n2. Dequeue\n3. Peek \n4. Display\n5. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        data = int(input("Enter data to enqueue: "))
        q.enqueue(data)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif(choice==4):
        q.display()
    else:
        print("Exiting...")
        break
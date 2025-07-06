#Queue is FIFO jsk jsg
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        #for the isnertion of elements into the queue i will use end insert
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
        else:
            a=self.head
            while a.next is not None:#i have to move upto the last location
                a=a.next#moving the pointer to the last location
            a.next=new_node#linking the last node to the new_node
    def dequeue(self):
        if(self.head is None):
            print('Hey Queue is Empty')
        else:
            a=self.head#assigning to a temporary variable
            self.head=a.next#moving the head to the next location
            #for deleting the node we have to assign the current node to None
            print(f'{a.data} is Deleted Successfully!')
            a.next=None
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
    def peek(self):
        if(self.head is None):
            print('Queue is empty')
        else:
            print(f'{self.head.data} is the peek element')
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
'''
Queue is a DS that follows the FIFO (First In First Out) property.
Operations:
- Enqueue: Add an element
- Dequeue: Remove an element
- Display: Show all elements
'''
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
        else:
            print('Queue is empty, cannot delete.')
    def display(self):
        if len(self.queue) > 0:
            print('=====' * 5)
            for i in self.queue:
                print(i, end=' ')
            print()
            print('=====' * 5)
        else:
            print('Queue is empty.')
q = Queue()
while True:
    print('\nQueue Operations:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        data = int(input("Enter data to enqueue: "))
        q.enqueue(data)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    else:
        print("Exiting...")
        break
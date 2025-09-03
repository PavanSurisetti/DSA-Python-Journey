#stack_using_arrays.py
#stack is a LIFO means last in first out ex: set of plates
''' 
we can perform the operations like:
1.Push-entering the elements
2.Pop-deleting the elements
3.peek-returns the top element without deleting it
4.display-Displaying the elements
'''
class stack:
    def __init__(self):
        self.items=[]#creating a stack using arrays
    def push(self,data):
        self.items.append(data)
        print(f'{data} inserted succesfully')
    def pop(self):
        if(len(self.items)==0):#there is no elements in the stack
            print('stack is empty')
        else:#some elements are there!
            popped=self.items.pop()
            print(f'{popped} deleted successfully')
    def peek(self):
        if(len(self.items)>0):
            ele=self.items[len(self.items)-1]
            print(f'this is the top element in the stack:{ele}')
        else:
            print('stack is empty')
    def display(self):
        print('----'*10)
        print('Current Stack contains:')
        if(len(self.items)==0):#there is no elements
            print('stack is empty')
        else:
            for i in self.items[::-1]:#it will display from the top to bottom
                print(i)
        print('----'*10)
    def length_of_stack(self):
        print(f'the length of the stack is :{len(self.items)}')
s=stack()
s.push(10)
s.display()
s.push(11)
s.display()
s.pop()
s.display()
s.peek()
s.length_of_stack()
s.pop()
s.peek()
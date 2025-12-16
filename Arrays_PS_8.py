'''  
Rotate Array by K Elements

Given an array of integers nums of size n and an integer k, rotate the array by k positions either to the left or to the right based on the given direction.

Left rotation: Elements are shifted to the left, and the first elements move to the end.

Right rotation: Elements are shifted to the right, and the last elements move to the beginning.

Input

An integer array nums

An integer k (number of rotations)

A string direction ("left" or "right")

Output

The array after rotating it by k positions in the specified direction.

Examples

Example 1
Input:
nums = [1, 2, 3, 4, 5, 6, 7], k = 2, direction = "right"

Output:
[6, 7, 1, 2, 3, 4, 5]

Example 2
Input:
nums = [1, 2, 3, 4, 5, 6], k = 2, direction = "left"

Output:
[3, 4, 5, 6, 1, 2]
'''
def check(n,k):
    k=k%len(n)
    directions=input('Enter L or R:').upper()
    if(directions=='L'):
            temp=n[k:]+(n[:k])
            print(f'Original :{n}->{temp}')
    elif(directions=='R'):
            temp=n[-k:]+(n[0:(len(n)-k)])
            print(f'Original :{n}->{temp}')
    else:
        print('Invalid Direction')
n=[1, 2, 3, 4, 5, 6, 7]
k=int(input('Enter No.Of.Rotations:'))
check(n,k)
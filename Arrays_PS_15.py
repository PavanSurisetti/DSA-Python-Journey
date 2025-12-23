'''
Leaders in an Array 

You are given an array of integers of size N.
An element in the array is called a leader if it is greater than or equal to all the elements to its right side.

The rightmost element of the array is always a leader because there are no elements to its right.

Your Task

Find and print all the leader elements in the given array.

Example

Input:
arr = [16, 17, 4, 3, 5, 2]

Output:
17 5 2

Explanation:

17 is greater than all elements to its right

5 is greater than 2

2 is the last element, so it is a leader
'''
# def check(n):#funtion to check the leader elements
#     leader=[]#creating a leader list
#     for i in range(len(n)):# traversing from the first to last and verifying 
#         big=n[i]#assuming current as big element
#         leader.append(n[i])
#         for j in range(i+1,len(n)):#moving to right side of current node
#             if(big>n[j]):
#                 pass
#             else:
#                 leader.remove(n[i])
#                 break
#     return leader
#the above code is ok but the complexity is o(n^2)
def check(n):
    l=len(n)
    maxright=n[-1]#always the last element is greater 
    result=[maxright]
    for i in range(l-2,-1,-1):
        ''' #here we are moving from left to right and 
        start value as last second element in array 
        because we need not to check the last element 
        so we start from the last second element'''
        if(n[i]>maxright):
            maxright=n[i]
            result.append(maxright)
    return result[::-1]#this is to get in the order from right to left
print(check(n=[16, 17, 4, 3, 5, 2]))
print(check(n= [4, 7, 1, 0]))
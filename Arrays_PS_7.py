'''
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Examples
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
'''
n=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
def check(n):
    # for i in range(len(n)):
    #     if(n[i]==0):
    #         n.pop(i)
    #         n.append(0)
    #the above code is not optimal
    c=n.count(0)#finding the total zeros
    n1=[]#new list of numbers
    for i in range(len(n)):
        if(n[i]!=0):
            n1.append(n[i])
    for i in range(c):#iterating the no of zeros appers
        n1.append(0)
    #instead of above loop u can also use this
    #n1.extend([0]*c) it will also results same
    return n1
print(check(n))
print(check([1,2,0,1,0,4,0]))
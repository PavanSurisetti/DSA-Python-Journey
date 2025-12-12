'''
Given an array of integers and a target value, write a program to find the index of the target value in the array using Linear Search.

If the target value exists in the array, return its index.

If the target value does not exist, return -1.

Example:
Input: arr = [4, 2, 7, 1, 9], target = 7
Output: 2
'''
def check(n,target):
    for i in range(len(n)):
        if(n[i]==target):
            return i
    return -1
nums = [4, 2, 7, 1, 9]
target = 7
print(check(nums,target=target))
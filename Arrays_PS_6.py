''' 
Maximum Consecutive Ones

Given a binary array (an array containing only 0s and 1s), find and return the maximum number of consecutive 1s present in the array.

Example:
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3
Explanation: The longest run of 1s is 1, 1, 1 → length = 3.
'''
def check(n):
    current=0#we need two count variables for checking
    maximum=0
    for i in range(len(n)):
        if(n[i]==1):
            current+=1
            maximum=max(current,maximum)
        else:
            current=0
    return maximum
print(check([1, 1,0, 1, 1, 1]))
print(check([1, 1, 1, 0, 1]))
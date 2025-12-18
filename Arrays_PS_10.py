#Find the missing number in an array
'''  
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array..
Examples
Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.
Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer.
'''
#in general if those are sets we can perform A-B then it will return the missing element
#but the sets are not optimal because it can create extra space.
def check(n):
    nl=len(n)+1
    expected_sum=(nl*(nl+1))//2
    totalsum=sum(n)
    return(expected_sum-totalsum)
print(check(n=[1,2,4,5]))
print(check([1,3]))
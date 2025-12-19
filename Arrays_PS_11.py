'''  
Find the number that appears once, and the other numbers twice
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
Examples
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.
Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

'''
n=[1,2,2]
# for i in n:
#     if(n.count(i)==1):
#         print(i)
#         break
#the above solution is ok but it is not optimal...
#x^x=0
#x^0=x
def check(n):
    ans=0
    for i in n:
        ans^=i
    return ans
print(check(n=n))
n=[4,1,2,1,2]
print(check(n=n))
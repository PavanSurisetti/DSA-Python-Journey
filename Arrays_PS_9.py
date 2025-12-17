''' 
Remove Duplicates In-Place from a Sorted Array
Problem Statement

You are given an integer array arr sorted in non-decreasing order.
Your task is to remove duplicate elements in-place such that each unique element appears only once, while maintaining the original relative order of the elements.

After removing the duplicates:

The first k elements of the array should contain the unique elements.

The function should return k, the number of unique elements.

The elements beyond the first k positions do not matter.
Examples
Example 1

Input:
arr = [1, 1, 2, 2, 2, 3, 3]

Output:
[1, 2, 3, _, _, _, _]
'''
# def check(n):
#     for i in n:
#         if(n.count(i)!=1):#count>1
#             n.remove(i)
#     return(n,len(n))
# print(check([1, 1, 2, 2, 2, 3, 3]))
# print(check([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
#above code can fail in some conditions
def check(n):
    k=1
    if(len(n)==0):
        return 0
    else:
        for i in range(1,len(n)):
            if(n[i]!=n[i-1]):
                n[k]=n[i]
                k+=1
    return(k,n[:k])#after k there will be some duplicates we are not removing them
print(check([1, 1, 2, 2, 2, 3, 3]))
print(check([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
'''
Left Rotate an Array by One Place

Given an array of integers, left-rotate the entire array by one position.

After rotation, the first element moves to the end.

All other elements shift one position to the left.

Return or print the new rotated array.

Example:
Input: arr = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
'''
n= [1, 2, 3, 4, 5]
n.append(n[0])
n.pop(0)
print(n)
# for i in range(len(n)-1):
#     n[i],n[i+1]=n[i+1],n[i]
# print(n)
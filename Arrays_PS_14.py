''' 
Search in a sorted 2D matrix
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively.
The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer target, and your task is to find if it exists in the given 'mat' or not.
Examples
Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
Output :True.
Explanation :The target = 8 exists in the 'mat' at index (1, 3).

Input :mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
Output :false.
Explanation :The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.
'''
n=[ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
def check(n,target):
    row=len(n)#no of rows
    col=len(n[0])#no of cols
    high=row*col-1  #n*m
    low=0
    while low<=high:
        mid=(low+high)//2
        rows=mid//col#this beacause each has 'col' elements 
        cols=mid%col#this because to give the position of a element in a matrix
        if target==n[rows][cols]:
            return True
        elif(target<n[rows][cols]):
            high=mid-1
        else:
            low=mid+1
    return False
print(check(n,target=90))
print(check(n,target=8))
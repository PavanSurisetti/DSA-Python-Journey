''' 
Union of Two Sorted Arrays
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.
NOTE: Elements in the union should be in ascending order.
Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
Output: {1,2,3,4,5}
'''
def check(l1,l2):
    i=j=0
    union=[]
    while i<len(l1) and j<len(l2):
        if(l1[i]<l2[j]):#first array element is lesser
            if not union or union[-1]!=l1[i]:# if it is None then append and also if the last the element is not same then not append;
                union.append(l1[i])
            i+=1
        elif(l1[i]>l2[j]):#second array element is lesser
            if not union or union[-1]!=l2[j]:# if it is None then append and also if the last the element is not same then not append;
                union.append(l2[j])
            j+=1
        else:  # l1[i] == l2[j]
            if not union or union[-1] != l1[i]:
                union.append(l1[i])
            i += 1
            j += 1
    while i<len(l1):
        if(union[-1]!=l1[i]):
            union.append(l1[i])
        i+=1
    while j<len(l2):
        if(union[-1]!=l2[j]):
            union.append(l2[j])
        j+=1
    return (union)
n1=[1,2,3,4,5]
n2=[2,3,4,4,5]
print(check(n1,n2))
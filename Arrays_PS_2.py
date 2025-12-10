'''
Given an array of size n, determine whether the array is sorted in non-decreasing (ascending) order.
Return True if it is sorted, otherwise return False.

Examples:

Input: N = 5, array = [1, 2, 3, 4, 5] → Output: True

Input: N = 5, array = [5, 4, 6, 7, 8] → Output: False
'''
class checking:
    def finding_sorted_or_not(self,nums):
        for i in range(len(nums)-1):#to avoid out of index error
           if(nums[i]>nums[i+1]):#check if i th position value is greater than i+1 th position value then it is not sorted
               return False
        return True#if it is in sorted order
c=checking()
print(c.finding_sorted_or_not([1, 2, 3, 4, 5]))
print(c.finding_sorted_or_not([5, 4, 6, 7, 8]))
'''
Problem Statement

Given an array of integers nums, return the second-largest element in the array.
If the second-largest element does not exist, return -1.

Examples

Input: nums = [8, 8, 7, 6, 5] → Output: 7

Input: nums = [10, 10, 10, 10, 10] → Output: -1

Input: nums = [7, 7, 2, 2, 10, 10, 10] → Output: 2 (second largest after 10)
'''
class secondLargest:
    def secondMax(self,nums):
        large=max(nums)
        new_list=[n for n in nums if n!=large]
        if(len(new_list)==0):
            return -1
        return max(new_list)
s=secondLargest()
print(s.secondMax([8, 8, 7, 6, 5]))
print(s.secondMax([10, 10, 10, 10, 10]))
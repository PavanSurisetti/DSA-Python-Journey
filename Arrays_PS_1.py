#Arrays_PS_1
'''
Given an array of integers nums, return the value of the largest element in the array.

Examples

Input: nums = [3, 3, 6, 1] → Output: 6

Input: nums = [3, 3, 0, 99, -40] → Output: 99

Input: nums = [-4, -3, 0, 1, -8] → Output: 1
 '''
class largestElement:
    def largestelement(self,nums):
        nums.sort()
        return (nums[-1])
s=largestElement()
print(s.largestelement([3, 3, 6, 1]))
print(s.largestelement([3, 3, 0, 99, -40]))
print(s.largestelement([-4, -3, 0, 1, -8]))
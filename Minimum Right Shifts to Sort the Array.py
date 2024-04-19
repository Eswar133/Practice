""" 
2855. Minimum Right Shifts to Sort the Array

You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of right shifts required to sort nums and -1 if this is not possible.

A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 2
Explanation: 
After the first right shift, nums = [2,3,4,5,1].
After the second right shift, nums = [1,2,3,4,5
"""
class Solution(object):
    def minimumRightShifts(self,nums):
        n = len(nums)
        for shifts in range(n):
            sortednums = sorted(nums)
            if sortednums == nums:
                return shifts 
            nums = [nums[(i+1)%n] for i in range(n)] 
        return -1
    
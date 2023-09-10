#https://leetcode.com/problems/sort-array-by-parity-ii/
"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 
"""

class solution(object):
    def sortArrayByParityII(self,nums):
        even,odd=0,1
        n=len(nums)
        while even<n and odd<n:
            while even<n and nums[even]%2==0:
                even+=2
            while odd<n and nums[odd]%2==1:
                odd+=2
            if even<n and odd<n:
                nums[even],nums[odd]=nums[odd],nums[even]
        return nums
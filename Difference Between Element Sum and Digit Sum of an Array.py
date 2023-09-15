#https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""
class Solution(object):
    def differenceOfSum(self, nums):
        sum1=0
        sum2=0
        for i in range(len(nums)):
            sum1+=nums[i]
            while nums[i]>0:
                sum2+=nums[i]%10
                nums[i]=nums[i]/10
        return abs(sum2-sum1)
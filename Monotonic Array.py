#https://leetcode.com/problems/monotonic-array/
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

class solution(object):
    def isMonotonic(self,nums):
        increasing=decreasing=True
        for i in range(len(nums)):
            if nums[i]>nums[i+1]:
                increasing=False
            elif nums[i]<nums[i+1]:
                decreasing=False
        return increasing or decreasing
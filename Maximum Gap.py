"""Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space."""


class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<=1:
            return 0
        nums.sort()
        difference=0
        maxdifference=0
        for i in range(1,len(nums)):
            difference = abs (nums[i] - nums[i-1]) 
            maxdifference=max(difference,maxdifference)
        return maxdifference
        
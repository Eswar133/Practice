""""
question:
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""
#question link:https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
class Solution(object):
    def targetIndices(self, nums, target):
        empty=[]
        nums.sort()
        for i ,num in enumerate(nums):
            if num==target:
                empty.append(i)
        return empty

        
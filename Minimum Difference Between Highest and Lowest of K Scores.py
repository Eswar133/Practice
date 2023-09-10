#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

 

"""

class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        minimum=10**5
        for i in range(len(nums)-k+1):
            currdiff=nums[i+k-1]-nums[i]
            minimum=min(currdiff,minimum)
        return minimum
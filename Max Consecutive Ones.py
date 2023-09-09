#https://leetcode.com/problems/max-consecutive-ones/
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_1s=0
        cur_1s=0
        for num in nums:
            if num ==1:
                cur_1s+=1
            else:
                max_1s=max(max_1s,cur_1s)
                cur_1s=0
        max_1s=max(max_1s,cur_1s)
        return max_1s
        
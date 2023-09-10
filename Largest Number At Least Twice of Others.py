#https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

"""
class solution(object):
    def dominantIndex(self,nums):
        max_number=max(nums)
        index_max=nums.index(max_number)
        for num in nums:
            if max_number!=num and max_number<2*num:
                return -1
        return index_max
#https://leetcode.com/problems/single-number-ii/description/
"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
 
"""
class Solution(object):
    def singleNumber(self, nums):
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for i,j in dict.items():
            if j==1:
                return i
        
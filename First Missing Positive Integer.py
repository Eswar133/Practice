#https://leetcode.com/problems/first-missing-positive/description/
"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 
"""



class solution(object):
    def firsMissingPositive(self,nums):
        set1=set(nums)
        missing=1
        for i in range(1,len(nums)+2):
            if i not in set1:
                missing=i
                break
        return  missing
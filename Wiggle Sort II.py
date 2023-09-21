#https://leetcode.com/problems/wiggle-sort-ii/description/
"""
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer. 
"""


class solution(object):
    def wiggleSort(self,nums):
        nums.sort()
        mid=len(nums[::2])-1
        nums[::2],nums[1::2]=nums[mid::-1],nums[:mid:-1]
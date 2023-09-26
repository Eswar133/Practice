#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
 
"""

class Solution(object):
    def searchRange(self, nums, target):
        left,right=0,len(nums)-1
        result=[-1,-1]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                result[0]=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                result[1]=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return result
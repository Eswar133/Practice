#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
 
"""

class Solution(object):
    def searchRange(self, nums, target):
        def binaryleft(nums,target):
            left,right=0,len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        def binaryright (nums,target):
            left,right=0,len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
            return right
        leftindex=binaryleft(nums,target)
        rightindex=binaryright(nums,target)
        if leftindex<=rightindex:
            return[leftindex,rightindex]
        else:
            return[-1,-1]
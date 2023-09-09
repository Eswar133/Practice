#https://leetcode.com/problems/minimum-common-value/
"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 
"""

class Solution(object):
    def getCommon(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)
        comman=set1.intersection(set2)
        if not comman:
            return -1

        return min(comman)
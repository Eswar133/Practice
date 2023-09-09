#https://leetcode.com/problems/merge-sorted-array/
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        target=[]
        p1,p2=0,0
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                target.append(nums1[p1])
                p1+=1
            else:
                target.append(nums2[p2])
                p2+=1
        while p1<m:
            target.append(nums1[p1])
            p1+=1
        while p2<n:
            target.append(nums2[p2])
            p2+=1
        nums1[:m+n]=target
        return nums1

        

        
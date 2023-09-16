#https://leetcode.com/problems/permutations/
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations=[]
        def backtrack(first):
            if first==len(nums):
                permutations.append(nums[:])

            for i in range(first,len(nums)):
                nums[first],nums[i]=nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i]=nums[i],nums[first]
        backtrack(0)
        return permutations
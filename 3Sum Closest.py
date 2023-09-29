#https://leetcode.com/problems/3sum-closest/description/
"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0). 
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums)==0:
            return sum(nums)
        nums.sort()
        cloest=float('inf')
        mindiff=float('inf')

        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                currsum=nums[i]+nums[left]+nums[right]
                diff=abs(target-currsum)
                if diff<mindiff:
                    mindiff=diff
                    cloest=currsum
                if mindiff==0:
                    return cloest
                if target>currsum:
                    left+=1
                else:
                    right-=1
        return cloest

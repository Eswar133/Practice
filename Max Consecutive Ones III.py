"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
   
"""

class Solution(object):
    def maxConsecutiveOnes(self,nums,k):
        left,zeros,maxlen,right=0,0,0,0,0
        n = len(nums)
        while right<n:
            if nums[right] == 0:
                zeros+=1
            if zeros>k:
                if nums[left] == 0:
                    zeros-=1
                left+=1
            if zeros<=k:
                currentlen = right-left+1
                maxlen = max(maxlen,currentlen)
        return maxlen
            
"""
1877.MinimizeMaximum Pair Sum in Array


The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

 

Example 1:

Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
"""
class Solution(object):
    def minPairSum(self,nums):
        n = len(nums)
        nums.sort()
        left,right=0,n-1
        min_maxsum = float('-inf')
        while left<right:
            pairsum = nums[left]+nums[right]
            min_maxsum = max(pairsum,min_maxsum)
            left+=1
            right-=1
        return min_maxsum
            
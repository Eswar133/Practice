#https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

"""
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

 

Example 1:

Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of 
"""

class Solution(object):
    def maxTripletProduct(self,nums):
        n = len(nums)
        max_product = float('-inf')  

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    product = (nums[i] - nums[j]) * nums[k]  
                    max_product = max(max_product, product)  

        if max_product < 0:
            return 0  
        else:
            return max_product


        
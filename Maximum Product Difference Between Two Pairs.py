#The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
#For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
#Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
#Return the maximum such product difference
#https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution(object):
    def maxProductDifference(self, nums):
        min1, min2 =10001,10002 
        max1, max2 = 0,0
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            
            if num >= max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        
        return abs(min1 * min2 - max1 * max2)

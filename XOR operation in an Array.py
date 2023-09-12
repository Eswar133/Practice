#https://leetcode.com/problems/xor-operation-in-an-array/
"""
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""

class Solution(object):
    def xorOperation(self, n, start):
        result=start
        for i in range(1,n):
            result^=start+2*i
        return result
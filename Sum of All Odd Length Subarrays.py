#https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

 
"""
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total_sum=0
        for length in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - length + 1):
                subarray = arr[i:i + length]
                total_sum += sum(subarray)
        
        return total_sum


        
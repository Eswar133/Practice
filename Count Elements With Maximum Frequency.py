"""


3005. Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements i 
"""
class solution(object):
    def maxfrequenceyElements(self,nums):
        freq = {}
        max1 = 0
        for num in nums:
            freq[num] = freq.get(num,0)+1
            max1 = max(max1,freq[num])
        count =0
        for i in freq.values():
            if i == max1:
                count+=1
        return count*max1
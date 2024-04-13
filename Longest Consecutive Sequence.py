"""
128.Longest Consecutive Sequence
Given an unsorted array of integers nums,return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time. 
"""
#1st approach
class Solution(object):
    def longestConsecutive(self,nums):
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        length = 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count+=1
            else:
                length = max(length,count)
                count = 1
        return max(length,count)
#2nd approach
class Solution(object):
    def longestconsecutive(self,nums):
        seen = set(nums)
        maxlen = 0
        for num in nums:
            if num-1 not in seen:
                currentnum = num
                currentlen = 1
                while currentnum+1 in seen:
                    currentnum+=1
                    currentlen+=1
                maxlen = max(maxlen,currentlen)
        return maxlen
        
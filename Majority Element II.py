#https://leetcode.com/problems/majority-element-ii/
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""
class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        list1=[]
        n=len(nums)
        for i ,j in dict.items():
            if j>n//3:
                list1.append(i)
        return list1
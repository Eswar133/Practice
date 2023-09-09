#Question:You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.Return the sum of all the unique elements of nums.
#https://leetcode.com/problems/sum-of-unique-elements/
class Solution(object):
    def sumOfUnique(self, nums):
        dict={}
        sum=0
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for key,value in dict.items():
            if value==1:
                sum+=key
        return sum
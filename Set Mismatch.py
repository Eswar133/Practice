#https://leetcode.com/problems/set-mismatch/description/
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""
class solution(object):
    def findErrorNums(self,nums):
        set1=set(nums)
        length=len(nums)
        for i in range(1,length+1):
            if i not in set1:
                missing=i
                break
        sum1=sum(nums)
        sum2=(length*(length+1))//2
        total=sum2-sum1
        return missing-total,missing
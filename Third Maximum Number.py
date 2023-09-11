#https://leetcode.com/problems/third-maximum-number/description/
"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
"""
class solution(object):
    def thirdMax(self,nums):
        firstmax=float('-inf')
        secondmax=float('-inf')
        thirdmax=float('-inf')
        for num in nums:
            if num>firstmax:
                thirdmax=secondmax
                secondmax=firstmax
                firstmax=num
            elif num>secondmax and num !=firstmax:
                thirdmax=secondmax
                secondmax=num
            elif num>thirdmax and num!=firstmax and num!=secondmax:
                thirdmax=num
        if thirdmax!=float('-inf'):
            return thirdmax
        
        else:
            return firstmax
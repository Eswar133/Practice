#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 
"""
class Solution(object):
    def sumZero(self, n):
        target=[]
        if n%2==1:
            target.append(0)
        for i in range(1,n//2+1):
            target.extend([i,-i])
        return target
        
        
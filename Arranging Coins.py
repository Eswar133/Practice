#https://leetcode.com/problems/arranging-coins/
"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""

class solution(object):
    def arrangeCoins(self,n):
        return int((2*n+0.25)**0.5-0.5)
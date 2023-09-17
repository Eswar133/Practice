#https://leetcode.com/problems/climbing-stairs/description/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
"""
class Solution(object):
    def climbStairs(self,n):
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]




        
        
"""Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
"""

class Solution(object):
    def judgeSquareSum(self, c):
        left,right=0,int(c ** 0.5)
        while left<=right:
            if (left**2+right**2) == c:
                return True
            elif (left**2 + right**2) > c:
                right-=1
            else:
                left+=1
        return False
        
        
"""

You are given two integers red and blue representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.

All the balls in a particular row should be the same color, and adjacent rows should have different colors.

Return the maximum height of the triangle that can be achieved.

 

Example 1:

Input: red = 2, blue = 4

Output: 3 
"""

class Solution(object):
    def maxHeightOfTriangle(self,red,blue):
        return max(self.helper(red,blue,True),self.helper(red,blue,False))
    
    def helper(self,red,blue,start_with_red):
        i = 0 # rows
        j=1#balls
        while True:
            if (i%2==0 and start_with_red) or (i%2==1 and not start_with_red):
                if red >= j:
                    red -= j
                else:
                    break
            else:
                if blue >= j:
                    blue -= j
                else:
                    break
            i+=1
            j+=1
        return i
        
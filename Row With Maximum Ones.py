#https://leetcode.com/problems/row-with-maximum-ones/
""" 
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.
"""
class solution (object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n=len(mat)
        m=len(mat[0])
        row,count=0,0
        for i in range (n):
            ones=0
            for j in range(m):
                if mat[i][j]==1:
                    ones+=1

                if ones>count:
                    count=ones

                    row=i
        return [row,count]
#https://leetcode.com/problems/h-index-ii/description/
""" 
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.
"""
class solution (object):
    def hIndex(self,citations):
        h=0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                h=i+1
            else:
                break
        return h
    
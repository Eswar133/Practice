#https://leetcode.com/problems/kth-missing-positive-number/
"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

"""

class solution(object):
    def findkthpositive(self,arr,k):
        miss=0
        count=1
        while miss<k:
            if count not in arr:
                miss+=1
            if miss<k:
                count+=1
        return count
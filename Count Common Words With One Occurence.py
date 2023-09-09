#https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
"""

class Solution(object):
    def countWords(self, words1, words2):
        count=0
        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1 and i in words2:
                count+=1

        return count

        
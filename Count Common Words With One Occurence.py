#https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
"""

class Solution(object):
    def countWords(self, words1, words2):
        dict1 = {}
        for word in words1:
            dict1[word] = dict1.get(word, 0) + 1
        

        dict2 = {}
        for word in words2:
            dict2[word] = dict2.get(word, 0) + 1
        

        count = 0
        for word, freq in dict1.items():
            if freq == 1 and dict2.get(word, 0) == 1:
                count += 1
        
        return count


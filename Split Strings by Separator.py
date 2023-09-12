#https://leetcode.com/problems/split-strings-by-separator/
"""
Given an array of strings words and a character separator, split each string in words by separator.

Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes

separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
A split may result in more than two strings.
The resulting strings must maintain the same order as they were initially given.
"""
class solution(object):
    def splitWordsByseparator(self,words,separator):
        result=[]
        for word in words:
            splitwords=[w for w in word.split(separator)if w]
            result.extend(splitwords)
        return result
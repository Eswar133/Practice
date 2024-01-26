#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 
"""
class Solution(object):
    def strStr(self, haystack, needle):
        lneedle=len(needle)
        lhaystack=len(haystack)
        for i in range(lhaystack):
            result=haystack[i:lneedle+i]
            if result==needle:
                return i
        return -1
                        
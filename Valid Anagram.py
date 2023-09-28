#https://leetcode.com/problems/valid-anagram/

""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        counts={}
        countt={}
        for char in s:
            counts[char]=counts.get(char,0)+1
        for char in t:
            countt[char]=countt.get(char,0)+1
        return counts==countt
        
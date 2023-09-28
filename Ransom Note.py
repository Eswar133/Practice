#https://leetcode.com/problems/ransom-note/
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true 
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine)<len(ransomNote):
            return False
        countm={}
        countr={}
        for char in magazine:
            countm[char]=countm.get(char,0)+1
        for char in ransomNote:
            countr[char]=countr.get(char,0)+1
            if countr[char]>countm.get(char,0):
                return False
        return True
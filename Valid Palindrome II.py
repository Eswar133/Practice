#https://leetcode.com/problems/valid-palindrome-ii/description/
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true

"""

class solution(object):
    def validPalindrome(self,s):
        def isPalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]<s[right]:
                return isPalindrome(left+1,right) or isPalindrome(left,right-1)
            left+=1
            right-=1
        return True
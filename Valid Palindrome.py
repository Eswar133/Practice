#https://leetcode.com/problems/valid-palindrome/description/
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class solution(object):
    def isPalindrome(self,s):
        clean_string= re.sub(r'[^a-zA-Z0-9]','',s)
        clean_string=clean_string.lower()
        n = len(clean_string)
        for i in range(n//2):
            if clean_string[i] != clean_string[n-1-i]:
                return False 
        return True
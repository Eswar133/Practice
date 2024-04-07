""""
678.Valid Parenthesis String


Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
"""
class Solution(object):
    def checkValidString(self,s):
        openmin = 0
        openmax = 0
        for char in s:
            if char =='(':
                openmin+=1
                openmax+=1
            elif char == ')':
                openmin-=1
                openmax-=1
            else:
                openmin-=1
                openmax+=1
            if openmax<0:
                return False
        return openmin == 0
    
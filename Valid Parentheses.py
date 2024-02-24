#https://leetcode.com/problems/valid-parentheses/description/
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true 
"""

class Solution(object):
    def isValid(self,s):
        list1=[]
        for i in s:
            if i == '[':
                list1.append(']')
            elif i == '{':
                list1.append('}')
            elif i == '(':
                list1.append(')')
            elif len(list1) == 0 or list1.pop() != i:
                return False
        return len(list1)==0

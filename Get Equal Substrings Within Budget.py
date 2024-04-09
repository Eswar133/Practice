"""
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3: 
"""
class Solution (object):
    def equalSubstring(self,s,t,maxCost):
        n = len(s)
        left = 0
        maxlength = 0
        currentcost = 0
        for right in range(n):
            currentcost += abs(ord(s[right])-ord(t[right]))
            while currentcost>maxCost:
                currentcost-=abs(ord(s[left])-ord(t[left]))
                left+=1
            maxlength = max(maxlength,right-left+1)
        return maxlength
            
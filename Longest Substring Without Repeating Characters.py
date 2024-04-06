"""
3:Longest Substring Without Repearing Characters

Given a string s, find the length of the longest substring witout repeating characters:
example:
input s= 'abcabcbb'
output: 3

    
"""
class Solution(object):
    def lengthOfLongestSubstring(self,s):
        m = 0
        l = 0
        seen =set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.removes[l]
                l+=1
            seen.add(s[r])
            m = max(m,r-l+1)
        return m
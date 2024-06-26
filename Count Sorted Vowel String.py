"""

1641. Count Sorted Vowel Strings

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
 
"""
class Solution(object):
    def countVowelStrings(self,n):
        dp = [[0]* 5 for _ in range(n)]#because the vowels are 5 a,e,i,o,u
        for i in range(5):
            dp[0][j] = 1
        for i in range(1,n):
            for j in range(5):
                dp[i][j] = dp[i-1][j] +(dp[i][j-1] if j>0 else 0)
        return sum(dp[-1])
    
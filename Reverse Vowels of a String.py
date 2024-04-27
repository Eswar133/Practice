"""


345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters 
"""
class Solution(object):
    def reverseVowels(self,s):
        word = list(s)
        left = 0
        right = len(word)-1
        vowels="AEIOUaeiou"
        while left<right:
            while left<right and vowels.find(word[left])==-1:
                left+=1
            while left<right and vowels.find(word[right])==-1:
                right-=1
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1
        return "".join(word) 
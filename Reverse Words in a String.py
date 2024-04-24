"""
151 . Reverse Words in a String 

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiples spaces between two words. 

returned string should only have a single space separating the words. Do not includeany extra spaces.

Example 1:
Input : s = "the sky is blue:

output: "blue is sky the"

Example 2:
Input s =" hello world"

output : "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.


Example 3:
Input : s = "a good example"

output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a 
single space in the reversed string

"""

class Solution(object):
    def reverseWords(self,s):
        words =s.split()
        reverse_words = words [::-1]
        reverse_string = ' '.join(reverse_words)
        return reverse_string
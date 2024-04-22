class Solution(object):
    def largestNumber(self,nums):
        sorted_str = ''.join(sorted(map(str,nums),key=lambda x:x*10,reverse=True))
        if sorted_str[0] == '0':#handling edge cases
            return '0'
        return sorted_str
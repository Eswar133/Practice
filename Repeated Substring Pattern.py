class Solution(object):
    def repeatedSubstringPattern(self,s):
        sfo = "".join((s[1:],s[:-1]))
        return s in sfo
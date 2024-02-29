class Solution(object):
    def semiOrderedPermutation(self,nums):
        n=len(nums)
        a=nums.index(1)
        b=nums.index(n)
        if a <b:
            return a + n - 1 - b 
        else:
            return a + n - 1 - b - 1
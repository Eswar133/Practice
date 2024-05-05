class Solution(object):
    def gcd(self,a,b):
        while b:
            a,b=b,a%b 
        return a 
    def subarrayLCM(self,nums,k):
        count = 0
        for i in range(len(nums)):
            lcm = nums[i]
            for j in range(i,len(nums)):
                lcm = lcm*nums[j]//self.gcd(nums[j],lcm)
                if lcm == k:
                    count+=1
        return count
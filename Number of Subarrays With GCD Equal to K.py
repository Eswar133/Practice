class solution(object):
    def gcd(self,a,b):
        while b:
            a,b=b,a%b 
        return a 
    def subarrayGCD(self,nums,k):
        count = 0
        for i in range(len(nums)):
            lc = nums[i]
            for j in range(i,len(nums)):
                lc = self.gcd(nums[j],lc)
                if lc == k:
                    count+=1
        return count 
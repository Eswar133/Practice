class Solution(object):
    def minimumRightShifts(self,nums):
        sorted_nums=nums.sort()
        n=len(nums)
        for shift in range(n):
            if nums==sorted_nums:
                return shift
            nums=[nums[-1]]+nums[:-1]
        return -1
    
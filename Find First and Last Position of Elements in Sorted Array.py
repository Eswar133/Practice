'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
#BruteForce
class Solution(object):
    def searchRange(self, nums, target):
        result=[]
        if len(nums) ==1 and target in nums:
            return [0,0]
        elif len(nums) <=1:
            return [-1,-1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                break 
            elif target not in nums:
                result.append(-1)
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                result.append(j)
                break
            elif target not in nums:
                result.append(-1)
                break
        return result
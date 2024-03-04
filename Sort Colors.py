#https://leetcode.com/problems/sort-colors/description/
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

  
"""

class solution(object):
    def sortColors(self,nums):
        curr,left,right=0,0,len(nums)-1
        while curr <= right:
            if nums[curr] == 0:
                nums[curr],nums[left] = nums[left],nums[curr]
                curr+=1
                left+=1
            elif nums[curr] ==2:
                nums[curr],nums[right] = nums [right],nums[curr]
                right-=1
            else:
                curr+=1
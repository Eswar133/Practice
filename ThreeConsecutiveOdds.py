#question:Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
#question_link:https://leetcode.com/problems/three-consecutive-odds/

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        
        for i in range(len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                return True
        return False
        
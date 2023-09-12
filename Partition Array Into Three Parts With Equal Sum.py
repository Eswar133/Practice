#https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])


"""
class solution (object):
    def canThreePartsEqualSum(self,arr):
        totalsum=sum(arr)
        if totalsum%3!=0:
            return False
        partsum=totalsum//3
        currsum=0
        count=0
        for num in arr:
            currsum+=num
            if currsum==partsum:
                count+=1
                currsum=0
            if count==3:
                return True
        return False
        
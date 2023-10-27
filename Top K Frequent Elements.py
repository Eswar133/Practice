#https://leetcode.com/problems/top-k-frequent-elements/
"""

 Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


class Solution(object):
    def topKFrequent(self,nums, k):
    
        frequency = {}
    

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
    
        result = []
    
    
        for _ in range(k):
        
            max_freq_element = None
            max_freq = -1
            for num, freq in frequency.items():
                if freq > max_freq:
                    max_freq = freq
                    max_freq_element = num
        
        
            result.append(max_freq_element)
        
        
            del frequency[max_freq_element]
    
    
        return result

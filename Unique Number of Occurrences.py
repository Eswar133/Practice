class Solution(object):
    def uniqueOccurrences(self,arr):
        dict1={}
        for num in arr:
            dict1[num]=dict1.get(num,0)+1
            occurences=set()
        for count in dict1.values():
            if count in occurences:
                return False 
            else:
                occurences.add(count)
        return True
            
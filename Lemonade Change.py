#https://leetcode.com/problems/lemonade-change/
"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 
"""

class Solution(object):
    def lemonadeChange(self, bills):
        change={5:0,10:0}
        for bill in bills:
            if bill==5:
                change[5]+=1
            elif bill==10:
                if change[5]>=1:
                    change[5]-=1
                    change[10]+=1
                else:
                    return False
            elif bill==20:
                if change[5]>=1 and change[10]>=1:
                    change[5]-=1
                    change[10]-=1
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
        return True
            
            

        
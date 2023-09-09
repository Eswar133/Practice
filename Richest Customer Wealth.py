#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#https://leetcode.com/problems/richest-customer-wealth/

class solution(object):
    def maximumWealth(self,account):
        return max(sum[acc]for acc in account)
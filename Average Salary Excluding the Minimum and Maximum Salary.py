#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""
class Solution(object):
    def average(self, salary):
        return ((sum(salary)-max(salary)-min(salary))/float(len(salary)-2))
       
        
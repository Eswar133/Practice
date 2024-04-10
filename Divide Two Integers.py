"""

29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
  
"""
class Solution(object):
    def divide(self, dividend, divisor):
        # Handle the edge case where the dividend is INT_MIN (-2^31) and divisor is -1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the result
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        # Initialize the quotient
        ans = 0
        
        # Take absolute values to work with positive numbers
        dvd = abs(dividend)
        dvs = abs(divisor)

        # Perform division using repeated subtraction
        while dvd >= dvs:
            # Initialize a multiplier for the divisor
            k = 1
            # Double the divisor until it exceeds or equals the remaining dividend
            while k * 2 * dvs <= dvd:
                k <<= 1
            # Subtract the largest multiple of the divisor from the remaining dividend
            dvd -= k * dvs
            # Update the quotient by adding the multiplier
            ans += k

        # Apply the sign to the quotient and return
        return sign * ans

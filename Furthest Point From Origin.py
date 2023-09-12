#https://leetcode.com/problems/furthest-point-from-origin/
"""
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.
"""


class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        a,b,c=0,0,0

        for move in moves:
            if move == "R":
                a += 1
            elif move == "L":
                b += 1
            elif move == "_":
                c += 1
        return abs(a-b)+c
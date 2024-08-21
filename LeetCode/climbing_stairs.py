# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# 70. Climbing Stairs
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45


# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# 1,1,2,3,5,
# create array containing 0 with length of n+1 which will contain number of ways which eventually is a fibonnaci
# intialize first two elements to 1 since there can only be 1 way to climb 0 or 1 stair
# iterate from 3rd element to n+1
    # set value of i to sum of previous two
# return value of last element


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        climb_ways =[0]*(n+1)
        climb_ways[0], climb_ways[1] = 1,1
        for i in range(2, n+1):
            climb_ways[i] = climb_ways[i-1] + climb_ways[i-2]
        
        return climb_ways[n]
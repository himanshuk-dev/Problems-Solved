# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# Minimum Size Subarray Sum
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# Initialize window size to inf
# initialize sum to 0
# iterate over array till its length
# set sum to sum of current sub array
# check if sum is greater than or equal to target
    # get current_subarray_size
    # get min of window size and current_subarray_size
    # remove start value from sum
    # move start
# if window size is not inf return it

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        window_size = float('inf')
        sum = 0

        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                current_subarray_size = end - start + 1
                window_size = min(window_size, current_subarray_size)
                sum -= nums[start]
                start += 1
        
        return window_size if window_size != float('inf') else 0
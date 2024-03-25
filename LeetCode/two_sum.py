# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the difference and index
        num_map = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference = target - num
            
            # If the difference is found in the map, return the current index and the found index
            if difference in num_map:
                return [num_map[difference], i]
            
            # Store the current number and its index in the map
            num_map[num] = i
            
        # If no solution is found, just return an empty list (or None, depending on requirements)
        return []



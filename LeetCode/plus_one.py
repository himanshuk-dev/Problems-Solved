# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# Input = [2,4,9] --> output = [2,5,0]
# no leading zeros
# no empty array
# 
# convert array to string and concatenate [2,4,9] --> '249'
# add 1 --> 250
# convert to array --> [2,5,0]


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = int(''.join(str(digit) for digit in digits))
        number += 1
        digits_plus = [int(digit) for digit in str(number)]

        return digits_plus







# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:

# -231 <= x <= 231 - 1
 
# Follow up: Could you solve it without converting the integer to a string?

# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------
# x = 121 => True
# if palindrome => True else False

#  negative number is not a palindrome
#  we need to solve this without converting integer to a string
 
#   so we can just reverse the number and check if this new number is equal to our original number
	

# 1. 	 if integer is less than 0 return False
# 2. 	 proceed only if x isInstance of int
# 3. 	 store original number
# 4. 	 reverse given integer
# 5. 	 check if reversed_int == original => return

# How to reverse integer?
# 	121 % 10 = 1
# 	=2
# 	=1
	
# 	reversed_number
# 	1
# 	12
# 	121
	
# 	x
# 	121 // 10 = 12
# 	=1
# 	=0


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if integer is less than 0 return False
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        if isinstance(x, int):
            while x > 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x = x // 10
            
            return reversed_num == original
# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# ()[]{}

# 1. create stack
# 2. iterate over s
# 3. check if its starting bracket
# 4. store it in stack
# 5. else 
# 			6. if stack is empty return False
# 			7. current_char = stack.pop()
# 			8. if current_char is'(':
# 						9. if char !=')' return False
# 			10. if current_char is'{':
# 						11. if char !='}' return False
# 				12. if current_char is'(':
# 						13. if char !=')' return False

# 		if stack is not empty return False
# 		return True



# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ')':
                        return False

                if current_char == '{':
                    if char != '}':
                        return False

                if current_char == '[':
                    if char != ']':
                        return False

        if stack:
            return False
        return True
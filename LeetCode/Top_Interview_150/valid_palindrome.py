# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# Valid Palindrome
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.



# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# remove non alphanumeric
# lowercase char
# check if reverse is equal --> true
# else false

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_cleaned = ''.join(char for char in s if char.isalnum()).lower()

        return s_cleaned[::-1] == s_cleaned
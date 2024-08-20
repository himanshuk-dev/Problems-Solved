# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# Input = 'Hello world' --> Ouput = 5
# empty? No
# 
# Soln 1:
# split string by space and covert to array
# get the last element in array 
# now convert this last element to string and get length of it
# Soln 2:
# step on string from end
    # if space at end, proceed further
# count these steps
# break loop on space
# return count

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        s_array = s.split() 
        last_element_len = len(s_array[-1])
        return last_element_len
    

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        step = len(s) - 1
        length = 0
        
        while step >= 0 and s[step] == ' ':
            step -= 1
            
        while step >= 0 and s[step] != ' ':
            length += 1
            step -= 1
            
        return length
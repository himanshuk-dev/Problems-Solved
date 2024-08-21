# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# Easy
# Topics
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.6M
# Submissions
# 2.9M
# Acceptance Rate
# 54.2%


# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# result array
# carry storage
# reverse both strings
# iterate till maximum of max length of string(s)
    # get digit a if i < len(a)
    # get digit b if i< len(b)
    # get total 
    # insert remainder of total / 2 to result
# update carry to carry //= 2
# return reverse of result
# 


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i<len(a) else 0
            digit_b = int(b[i]) if i<len(b) else 0

            total = digit_a + digit_b + carry
            
            result.append(str(total % 2))
            
            carry = total // 2
        
        if carry:
            result.append('1')
            
        return ''.join(result[::-1])
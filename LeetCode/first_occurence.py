# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------
# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.



# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# 1. get te length of needle
# 2. step on string haystack till its length
# 3.get the string value in temp till length of needle starting from current step
# 4. if temp is equal to needle return this step or index
# 5. otherwise return -1


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length = len(needle)

        for index in range(len(haystack)):
            temp = haystack[index:needle_length+index]

            if temp == needle:
                return index
            
        return -1
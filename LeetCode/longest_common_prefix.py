# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

#  []? yes
 
#  return ""
 
#   ["flower","flow","flight"]
# 	flow, flower, flight
	
# 1. sort the array
# 2.store the first item in array to string1
# 3. store the last item in array to string2
# 4. index = 0
# 5. loop over these strings while index <len(string1) and len(string2)
# 				6. if the value matches, incement index
# 				7. else exit
# 8. string1[:index-1:1]


# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        strs.sort()

        string1 = strs[0]
        string2 = strs[- 1]

        index = 0

        while index < len(string1) and index < len(string2)-1:
            if string1[index] == string2[index]:
                index += 1
            else:
                break

        
        return string1[:index]
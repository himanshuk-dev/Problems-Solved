# -----------------------------------------------------------------------------
# Problem
# -----------------------------------------------------------------------------


# Code
# Testcase
# Test Result
# Test Result
# 664. Strange Printer
# Hard
# Topics
# Companies
# There is a strange printer with the following two special properties:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

 

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.


# -----------------------------------------------------------------------------
# PsuedoCode
# -----------------------------------------------------------------------------

# 1. Base Case: If i == j, it means we're dealing with a single character, so dp[i][j] = 1.
# 2. Recurrence Relation:
# - If s[i] == s[j], then the last character s[j] can be included in the same printing turn as s[i], so dp[i][j] = dp[i][j-1].
# - If s[i] != s[j], then we need to find a split point k where i <= k < j, and calculate the number of turns by splitting into two parts: dp[i][j]=min⁡(dp[i][k]+dp[k+1][j])dp[i][j] = \min(dp[i][k] + dp[k+1][j])dp[i][j]=min(dp[i][k]+dp[k+1][j])
# 1. Final Answer: The value dp[0][n-1] will give us the answer, where n is the length of the string s.

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1  # Base case: one character
        
        for length in range(2, n+1):  # length of the substring
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j-1])
        
        return dp[0][n-1]

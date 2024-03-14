# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 
# 
# 

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Initialize DP array with 0's, dp[0] = 1 since one way to make up amount 0 is using no coins
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # Iterate over each coin
        for coin in coins:
            # Update dp array for all amounts >= coin value
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount]

    # Example usage
    amount = 5
    coins = [1, 2, 5]
    print(change(amount, coins))
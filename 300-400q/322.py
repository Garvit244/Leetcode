'''
	You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

	Example 1:
	coins = [1, 2, 5], amount = 11
	return 3 (11 = 5 + 5 + 1)

	Example 2:
	coins = [2], amount = 3
	return -1.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
        	return 0

        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for val in range(1, amount+1):
        	for coin in coins:
        		if coin <= val:
        			dp[val] = min(dp[val-coin]+1, dp[val])
        return dp[amount] if dp[amount] != float('inf') else -1
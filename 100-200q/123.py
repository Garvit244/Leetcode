'''
	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete at most two transactions.

	Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

	Example 1:

	Input: [3,3,5,0,0,3,1,4]
	Output: 6
	Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
	             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
        	return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(3)]
        for i in range(1,3):
        	maxDiff = -prices[0]
        	for j in range(1,len(prices)):
        		dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
        		maxDiff = max(maxDiff, dp[i-1][j] -prices[j])

        return dp[2][len(prices)-1]


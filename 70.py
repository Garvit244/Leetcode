'''
	You are climbing a stair case. It takes n steps to reach to the top.

	Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

	Note: Given n will be a positive integer.

	Example 1:

	Input: 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0

        dp = [0]*n
        dp[0], dp[1] = 1, 2

        for index in range(2, n):
        	dp[index] = dp[index-1] + dp[index-2]
        return dp[n-1]

# Time: O(N)
# Space: O(N)

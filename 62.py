'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for index in range(m):
        	dp[index][0] = 1

        for index in range(n):
        	dp[0][index] = 1

        for index_i in range(1, m):
        	for index_j in range(1, n):
        		dp[index_i][index_j] = dp[index_i-1][index_j] + dp[index_i][index_j-1]

        return dp[m-1][n-1]
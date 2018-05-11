'''
	Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

	Note: You can only move either down or right at any point in time.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
        	return 0

        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]

        for index in range(1, row):
        	dp[index][0] = dp[index-1][0] + grid[index][0]

        for index in range(1, col):
        	dp[0][index] = dp[0][index-1] + grid[0][index]

        print dp
        for index_i in range(1, row):
        	for index_j in range(1, col):
        		dp[index_i][index_j] = min(dp[index_i-1][index_j], dp[index_i][index_j-1]) + grid[index_i][index_j]

        return dp[row-1][col-1]
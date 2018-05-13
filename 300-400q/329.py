'''
    Given an integer matrix, find the length of the longest increasing path.

    From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

    Example 1:

    nums = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    Return 4
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        result = 0
        dp = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result = max(result, self.dfs(matrix, dp, row, col))
                
        return result
    
    def dfs(self, matrix, dp, i, j):
        if dp[i][j]:
            return dp[i][j]
        max_depth = 0
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in direction:
            x, y = i + d[0], j + d[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j] :
                max_depth = max(max_depth, self.dfs(matrix, dp, x, y))
                
        dp[i][j] = max_depth + 1
        return dp[i][j]
        
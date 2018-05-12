class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        row, col = len(s), len(t)

        if col > row:
        	return 0

        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for r in range(row+1):
        	for c in range(col+1):
        		if r == 0 and c == 0:
        			dp[r][c] = 1
        		elif r == 0:
        			dp[r][c] = 0
        		elif c == 0:
        			dp[r][c] = 1
        		else:
        			dp[r][c] = dp[r-1][c]
        			if s[r-1] == t[c-1]:
        				dp[r][c] += dp[r-1][c-1]
        return dp[row][col] 

# Time: O(N^2)
# Space: O(N^2)
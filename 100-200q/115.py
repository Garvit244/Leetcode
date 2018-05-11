'''
    Given a string S and a string T, count the number of distinct subsequences of S which equals T.

    A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

    Example 1:

    Input: S = "rabbbit", T = "rabbit"
    Output: 3
    Explanation:

    As shown below, there are 3 ways you can generate "rabbit" from S.
    (The caret symbol ^ means the chosen letters)

    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^
'''

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
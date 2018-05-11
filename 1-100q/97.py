'''
	Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

	Example 1:

	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
	Output: true
	Example 2:

	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
	Output: false
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        if len(s3) != len(s1) + len(s2):
        	return False

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for row in range(len(s1)+1):
        	for col in range(len(s2)+1):
        		if row == 0 and col == 0:
        			dp[row][col] = True 
        		elif row == 0:
        			dp[row][col] =dp[row][col-1] and s2[col-1] == s3[row+col-1]
        		elif col == 0:
        			dp[row][col] = dp[row-1][col] and s1[row-1] == s3[row+col-1]
        		else:
        			dp[row][col] = (dp[row][col-1] and s2[col-1] == s3[row+col-1]) or (dp[row-1][col] and s1[row-1] == s3[row+col-1])

        return dp[len(s1)][len(s2)]

# Time: O(m*n)
# Space: O(m*n)
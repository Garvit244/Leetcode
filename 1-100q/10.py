'''
	Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.
	The matching should cover the entire input string (not partial).

	Note:

	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

 		for index in range(1, len(dp[0])):
            if p[index-1] == '*':
                dp[0][index] = dp[0][index - 2]
                
        for index_i in range(1, len(dp)):
        	for index_j in range(1, len(dp[0])):
        		if s[index_i - 1] == p[index_j - 1] or p[index_j - 1] == '.':
        			dp[index_i][index_j] = dp[index_i-1][index_j-1]
        		elif p[index_j-1] == '*':
        			dp[index_i][index_j] = dp[index_i][index_j-2]

        			if s[index_i-1] == p[index_j-2] or p[index_j-2] == '.':
        				dp[index_i][index_j] = dp[index_i-1][index_j] or dp[index_i][index_j]

        		else:
        			dp[index_i][index_j] = False


        return dp[len(s)][len(p)]
        
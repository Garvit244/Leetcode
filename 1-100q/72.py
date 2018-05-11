'''
	Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

	You have the following 3 operations permitted on a word:

	Insert a character
	Delete a character
	Replace a character
	Example 1:

	Input: word1 = "horse", word2 = "ros"
	Output: 3
	Explanation: 
	horse -> rorse (replace 'h' with 'r')
	rorse -> rose (remove 'r')
	rose -> ros (remove 'e')
	Example 2:

	Input: word1 = "intention", word2 = "execution"
	Output: 5
	Explanation: 
	intention -> inention (remove 't')
	inention -> enention (replace 'i' with 'e')
	enention -> exention (replace 'n' with 'x')
	exention -> exection (replace 'n' with 'c')
	exection -> execution (insert 'u')
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m , n = len(word1), len(word2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for index_i in range(m+1):
        	for index_j in range(n+1):
        		if index_i == 0:
        			dp[index_i][index_j] = index_j
        		elif index_j == 0:
        			dp[index_i][index_j] = index_i
        		elif word1[index_i-1] == word2[index_j-1]:
        			dp[index_i][index_j] = dp[index_i-1][index_j-1]
        		else:
        			dp[index_i][index_j] = 1 + min(dp[index_i-1][index_j], dp[index_i-1][index_j-1], dp[index_i][index_j-1])

        return dp[m][n]
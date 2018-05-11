'''
	 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

	For example, given n = 3, a solution set is:

	[
	  "((()))",
	  "(()())",
	  "(())()",
	  "()(())",
	  "()()()"
	]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        def backtracking(S, left, right):
        	if len(S) == 2*n:
        		result.append(S)
        		return 

        	if left < n:
        		backtracking(S+'(', left+1, right)

        	if right < left:
        		backtracking(S+')', left, right+1)

        backtracking('', 0, 0)
        return result
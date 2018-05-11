'''
	Given a 2D board and a word, find if the word exists in the grid.

	The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

	Example:

	board =
	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]

	Given word = "ABCCED", return true.
	Given word = "SEE", return true.
	Given word = "ABCB", return false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        result = False
        for row in range(len(board)):
        	for col in range(len(board[0])):
        		if self.dfs(board, word, row, col, 0):
        			return True
        return False

    def dfs(self, board, word, row, col, curr_len):
    	if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
    		return False
    	if board[row][col] == word[curr_len]:
    		c = board[row][col]
    		board[row][col] = '#'

    		if curr_len == len(word) - 1:
    			return True
    		elif (self.dfs(board, word, row-1, col, curr_len+1) or self.dfs(board, word, row+1, col, curr_len+1) or self.dfs(board, word, row, col-1, curr_len+1) or self.dfs(board, word, row, col+1, curr_len+1)):
    			return True

    		board[row][col] = c
    	return False
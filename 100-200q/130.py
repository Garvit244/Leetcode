'''
	Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

	A region is captured by flipping all 'O's into 'X's in that surrounded region.

	Example:

	X X X X
	X O O X
	X X O X
	X O X X
	After running your function, the board should be:

	X X X X
	X X X X
	X X X X
	X O X X
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
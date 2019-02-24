'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
'''

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        rook_index = (0, 0)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    rook_index = (row, col)
                    break
               
        flag = True
        col = rook_index[1]-1
        pawn = 0
        while col >= 0:
            if board[rook_index[0]][col] == 'B':
                flag = False
                break
            if board[rook_index[0]][col] == 'p':
                pawn += 1
                break
            col -= 1
        if flag and pawn != 0:
            result += 1
            
        flag = True
        col = rook_index[1]+1
        pawn = 0
        while col < len(board[0]):
            if board[rook_index[0]][col] == 'B':
                flag = False
                break
            if board[rook_index[0]][col] == 'p':
                pawn += 1
                break
            col += 1
            
        if flag and pawn != 0:
            result += 1
        
        flag = True
        row = rook_index[0]+1
        pawn = 0
        while row < len(board):
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
                
            if board[row][rook_index[1]] == 'p':
                pawn += 1
                break
            row += 1
            
        if flag and pawn != 0:
            result += 1
            
        pawn = 0
        flag = True
        row = rook_index[0]-1
        while row >= 0:
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
            if board[row][rook_index[1]] == 'p':
                pawn += 1
                break
            row -= 1
        if flag and pawn != 0:
            result += 1
        
        return result
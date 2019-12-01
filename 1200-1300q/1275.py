'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check(grid):
            for x in range(3):
                row = set([grid[x][0],grid[x][1],grid[x][2]])
                if len(row) == 1 and grid[x][0] != 0:
                    return grid[x][0]

            for x in range(3):
                column = set([grid[0][x],grid[1][x],grid[2][x]])
                if len(column) == 1 and grid[0][x] != 0:
                    return grid[0][x]

            diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
            diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
            if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
                return grid[1][1]

            return 0
        
        if not moves:
            return ""
        grid = [[0, 0, 0], [0, 0, 0], [0,0,0]]
        user = 1
        for move in moves:
            grid[move[0]][move[1]] = user
            if user == 1:
                user = 2
            else:
                user = 1
    
        result = check(grid)
        if result == 1:
            return "A"
        elif result == 2:
            return "B"
        else:
            if len(moves) == 9:
                return "Draw"
            else:
                return "Pending"

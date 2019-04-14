'''
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
'''

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        result = 0
        queue = []
        for row in range(len(A)):
            for col in range(len(A[0])):
                result += A[row][col]
                if (row*col == 0 or row == len(A)-1 or col == len(A[0])-1) and A[row][col] == 1:
                    queue.append((row, col))
                    
        x_move = [-1, 0, 1, 0]
        y_move = [0, 1, 0, -1]
        
        while queue:
            x, y = queue.pop(0)
            A[x][y] = 0
            result -= 1
            
            for xm, ym in zip(x_move, y_move):
                nx = x + xm
                ny = y + ym
                
                if 0<= nx <len(A) and 0 <= ny < len(A[0]) and A[nx][ny] == 1 and (nx, ny) not in queue:
                    queue.append((nx, ny))

        return result

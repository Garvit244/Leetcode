class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        index = []
        
        def around(i, j, board):
            count = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if 0<=k < len(board) and 0 <= l < len(board[0]):
                        if board[k][l] == 1:
                            count += 1
                            
            return count-1 if board[i][j] == 1 else count
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = around(i, j, board)
                if board[i][j] == 1:
                    if count > 3 or count < 2:
                        index.append([i, j, 0])
                else:
                    if count == 3:
                        index.append([i, j, 1])
                    
        while index:
            i, j, value = index.pop()
            board[i][j] =value
            
        
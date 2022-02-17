class Solution:
    def solveSudoku(self, bo):
        """
        Do not return anything, modify board in-place instead.
        """
        find = self.find_empty(bo)
        
        if not find:
            return True # solution found
        
        row, col = find
        
        for num in range(1, 10):
            if self.is_valid(bo, row, col, num):
                bo[row][col] = str(num)
                
                if self.solveSudoku(bo):
                    return True
                
                bo[row][col] = "."
        
        return False
    
    def find_empty(self, bo):
        for x in range(len(bo)):
            for y in range(len(bo[x])):
                if bo[x][y] == ".":
                    return (x, y)
    
    def is_valid(self, bo, row, col, val):
        val = str(val)
        # check row and col
        for x in range(len(bo)):
            for y in range(len(bo[x])):
                if bo[x][col] == val and x != row or bo[row][y] == val and y != col:
                    return False
        
        # check 3x3 box
        box_x = row // 3
        box_y = col // 3
        
        for x in range(box_x * 3, box_x * 3 + 3):
            for y in range(box_y * 3, box_y * 3 + 3):
                if bo[x][y] == val and (x, y) != (row, col):
                    return False
        
        return True
    
    
'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''

class Solution(object):
    def valid(self, row, col, row_size, col_size):
        return row >= 0 and col >= 0 and row < row_size and col < col_size
    
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        for row_index in range(len(grid)):
        	for col_index in range(len(grid[0])):
        		if grid[row_index][col_index] == 2:
        			queue.append((row_index, col_index))

        result = 0
        queue.append((-1, -1))
        while queue:
        	flag = False
        	print queue
        	while(queue[0][0] != -1 and queue[0][1] != -1):
        		(row, col) = queue[0]
        		if self.valid(row+1, col, len(grid), len(grid[0])) and grid[row+1][col] == 1 :
        			if not flag:
        				result += 1
        				flag =True
        			grid[row+1][col] = 2
        			row += 1
        			queue.append((row, col))
        			row -= 1
        		if self.valid(row-1, col, len(grid), len(grid[0])) and grid[row-1][col] == 1 :
        			if not flag:
        				result += 1
        				flag =True
        			grid[row-1][col] = 2
        			row -= 1
        			queue.append((row, col))
        			row += 1
        		if self.valid(row, col+1, len(grid), len(grid[0])) and grid[row][col+1] == 1 :
        			if not flag:
        				result += 1
        				flag =True
        			grid[row][col+1] = 2
        			col += 1
        			queue.append((row, col))
        			col -= 1
        		if self.valid(row, col-1, len(grid), len(grid[0])) and grid[row][col-1] == 1 :
        			if not flag:
        				result += 1
        				flag =True
        			grid[row][col-1] = 2
        			col -= 1
        			queue.append((row, col))
        			col += 1
        		queue.pop(0)
        	queue.pop(0)
        	if queue:
        		queue.append((-1, -1))
        for row_index in range(len(grid)):
        	for col_index in range(len(grid[0])):
        		if grid[row_index][col_index] == 1:
        			return -1
        return result

    
    
    
    
'''
Alternative Solution
'''


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        minutes = 0
        found1 = False
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    found1 = True
        
        if not found1: return 0
        if not queue: return -1
        queue.append((None, None))
        
        while queue:
            row, col = queue.popleft()
            if row is None and col is None:
                if queue:
                    queue.append((None, None))
                    minutes += 1
            else:
                if row + 1 < len(grid) and grid[row + 1][col] not in [2, 0]:
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                if row - 1 >= 0 and grid[row - 1][col] not in [2, 0]:
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                if col + 1 < len(grid[0]) and grid[row][col + 1] not in [2, 0]:
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                if col - 1 >= 0 and grid[row][col - 1] not in [2, 0]:
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
                
        return minutes
        

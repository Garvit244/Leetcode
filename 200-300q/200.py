class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
        	return 0

        count = 0
        for row in range(len(grid)):
        	for col in range(len(grid[0])):
        		if grid[row][col] == '1':
        			count +=1
        			self.merge(grid, row, col)

        return count

    def merge(self, grid, row, col):
    	if 0 > row or row >= len(grid) or col < 0 or col >= len(grid[0]):
    		return

    	if grid[row][col] != '1':
    		return 

    	grid[row][col] = '#'
    	self.merge(grid, row+1, col)
    	self.merge(grid, row-1, col)
    	self.merge(grid, row, col+1)
    	self.merge(grid, row, col-1)

'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''


class Solution(object):
	def shortestDistance(self, grid):
		if not grid:
			return -1

		def bfs(grid, distance_reach_map, row, col):
			if(row < 0 or row > len(grid) or col < 0 or col > len(grid[0])):
				return
			queue = [[row, col]]
			qdist = [1]

			direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
			while queue:
				x, y = queue.pop(0)
				curr_dist = qdist.pop(0)

				for dx, dy in direction:
					new_x, new_y = x+dx, y+dy
					if((0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and grid[new_x][new_y] == 0):
						grid[new_x][new_y] = -1
						queue.append([new_x, new_y])

						
						temp = distance_reach_map[new_x][new_y]
						dist, reach = temp[0], temp[1]
						dist += curr_dist
						reach += 1
						distance_reach_map[new_x][new_y] = [dist, reach]
						qdist.append(curr_dist+1)

			for row in range(len(grid)):
				for col in range(len(grid[0])):
					if grid[row][col] == -1:
						grid[row][col] =0

		r_len, c_len = len(grid), len(grid[0])
		distance_reach_map = [[[0, 0]]*c_len for _ in range(r_len)]
		buildings = 0
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == 1:
					bfs(grid, distance_reach_map, row, col)
					buildings += 1

		result = float('inf')
		for row in range(r_len):
			for col in range(c_len):
				dist, reach = distance_reach_map[row][col]
				if reach == buildings:
					result = min(result, dist)
		return result

solution = Solution()
grid = [[1, 0, 2, 0, 1], 
		[0, 0, 0, 0, 0], 
		[0, 0, 1, 0 ,0]]
print solution.shortestDistance(grid)






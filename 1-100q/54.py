'''
	Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

	Example 1:

	Input:
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
	Output: [1,2,3,6,9,8,7,4,5]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
        	return []

        R, C = len(matrix), len(matrix[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        result = []
        seen = [[False]*C for _ in range(R)]
        row = 0
        col = 0
        di = 0
        for _ in range(R*C):
        	result.append(matrix[row][col])
        	seen[row][col] = True
        	rr, cc = row + dr[di], col + dc[di]
        	if 0 <= rr < R and 0 <= cc < C and not seen[rr][cc]:
        		row, col = rr, cc
        	else:
        		di = (di+1)%4
        		row, col = row + dr[di], col + dc[di]

        return result
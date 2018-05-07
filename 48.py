'''
	You are given an n x n 2D matrix representing an image.

	Rotate the image by 90 degrees (clockwise).
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n%2 == 0:
        	m = n/2
        else:
        	m = n/2 + 1

        for i in range(n/2):
        	for j in range(m):
        		temp = matrix[i][j]
        		matrix[i][j] = matrix[n-j-1][i]
        		matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
        		matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
        		matrix[j][n-i-1] = temp

'''
	Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.
	Example 1:

	Input:
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 3
	Output: true
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
        	return 0
        left, right = 0, len(matrix[0])-1

        while left < len(matrix) and right >= 0:
        	if matrix[left][right] == target:
        		return True 
        	elif matrix[left][right] < target:
        		left += 1
        	else:
        		right -= 1
        return False
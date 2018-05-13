'''
	Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

	Note that it is the kth smallest element in the sorted order, not the kth distinct element.

	Example:

	matrix = [
	   [ 1,  5,  9],
	   [10, 11, 13],
	   [12, 13, 15]
	],
	k = 8,

	return 13.
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        if not matrix:
        	return 0 

        import heapq
        heap = []
        for col in range(len(matrix[0])):
        	heapq.heappush(heap, (matrix[0][col], 0, col))

        val = 0
        for index in range(k):
        	val, row, col = heapq.heappop(heap)
        	new_val = float('inf')
        	if row < len(matrix)-1:
        		new_val = matrix[row+1][col]
        	heapq.heappush(heap, (new_val, row+1, col))
        return val
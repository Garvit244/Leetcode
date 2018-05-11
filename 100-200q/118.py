'''
	Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

	Example:

	Input: 5
	Output:
	[
	     [1],
	    [1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row in range(numRows):
        	new_row = [0 for _ in range(row+1)]
        	new_row[0], new_row[-1] = 1, 1

        	for col in range(1, len(new_row)-1):
        		new_row[col] = triangle[row-1][col-1] + triangle[row-1][col]
        	triangle.append(new_row)
        return triangle
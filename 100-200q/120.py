'''
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

    For example, given the following triangle

    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        columns = len(triangle[length-1])
        
        matrix = [[ 0 for col in range(columns)] for row in range(length)]
        row_index = 0
        
        for row in range(length):
            elements = triangle[row]
            col_index = 0
            
            for val in elements:
                matrix[row_index][col_index] = val
                col_index += 1
            row_index += 1
            
        for row in range(length-2, -1, -1):
            for col in range(row+1):
                matrix[row][col] += min(matrix[row+1][col+1], matrix[row+1][col])
        return matrix[0][0]
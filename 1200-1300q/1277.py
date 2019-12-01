'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """  
    
        p_arr = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]  
        result = 0

        for index_i in range(1, len(matrix)):
            for index_j in range(1, len(matrix[0])):
                if matrix[index_i][index_j] == 1:
                    matrix[index_i][index_j] = min(matrix[index_i-1][index_j-1], min(matrix[index_i-1][index_j], matrix[index_i][index_j-1]))+1
        # print p_arr
        return sum([ sum(x) for x in matrix])  
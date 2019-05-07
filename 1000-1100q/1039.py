'''
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

 

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:

3 - 7	3 -	7
| / |	| \ |
5 - 4	5 -	4

Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 

Note:

3 <= A.length <= 50
1 <= A[i] <= 100
'''

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        for length in range(n):
            index_i = 0
            for index_j in range(length, n):
                if index_j < index_i+2:
                    dp[index_i][index_j] = 0
                else:
                    dp[index_i][index_j] = float('inf')
                    for index_k in range(index_i+1, index_j):
                        val = dp[index_i][index_k] + dp[index_k][index_j] + (A[index_i]*A[index_k]*A[index_j])
                        dp[index_i][index_j] = min(dp[index_i][index_j], val)
                index_i += 1
        return dp[0][n-1]

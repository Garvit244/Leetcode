'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j], and the line we draw does not intersect any other connecting (non-horizontal) line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
'''

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0]*len(A) for _ in range(len(B))]
        
        dp[0][0] = 1 if A[0] == B[0] else 0
        for index_i in range(1, len(dp)):
            dp[index_i][0] = dp[index_i-1][0]
            if A[0] == B[index_i]:
                dp[index_i][0] = 1
                
        for index_j in range(1, len(dp[0])):
            dp[0][index_j] = dp[0][index_j-1]
            if B[0] == A[index_j]:
                dp[0][index_j] = 1
                
        for index_i in range(1, len(dp)):
            for index_j in range(1, len(dp[0])):
                if A[index_j] == B[index_i]:
                    dp[index_i][index_j] = max(dp[index_i-1][index_j-1] + 1, max(dp[index_i-1][index_j], dp[index_i][index_j-1]))
                else:
                    dp[index_i][index_j] = max(dp[index_i-1][index_j-1], max(dp[index_i-1][index_j], dp[index_i][index_j-1]))
        return dp[len(B)-1][len(A)-1]

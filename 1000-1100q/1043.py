'''
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
'''

class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0
        
        N = len(A)
        dp = [0]*(N+1)
        for index_i in range(N):
            maxi = 0
            for index_j in range(index_i, index_i-K, -1):
                if index_j >= 0 and index_j < len(A):
                    maxi = max(maxi, A[index_j])
                    
                    dp[index_i+1] = max(dp[index_i+1], maxi*(index_i-index_j+1)+dp[index_j])
            # print index_i, maxi
            # print dp
                    
        return dp[-1]

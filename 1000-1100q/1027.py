'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
'''

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict

        dp = defaultdict(int)
        # print dp
        for index_i in range(len(A)):
            for index_j in range(index_i):
                diff = A[index_i] - A[index_j]
                dp[(index_i, diff)] = max(dp[(index_i, diff)], dp[(index_j, diff)]+1)
                # print dp
        return max(dp.itervalues())+1

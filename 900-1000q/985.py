'''
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 

Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
'''

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = 0
        for val in A:
            if val%2 == 0:
                result += val
        
        f_result = []
        for val_index in queries:
            val, index = val_index[0], val_index[1]
            prev_val = A[index]
            if prev_val%2 == 0:
                result -= prev_val
            new_val = prev_val + val
            if new_val %2 == 0:
                result += new_val
            A[index] = new_val
            f_result.append(result)
        return f_result
 
'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        j = 0
        while j <N and A[j] < 0:
            j += 1
        i = j-1
        result = []
        while i >= 0 and j < N:
            if A[i]**2 < A[j]**2:
                result.append(A[i]**2)
                i -= 1
            else:
                result.append(A[j]**2)
                j += 1
        while i>= 0:
            result.append(A[i]**2)
            i -= 1
            
        while j < N:
            result.append(A[j]**2)
            j += 1
                
        return result

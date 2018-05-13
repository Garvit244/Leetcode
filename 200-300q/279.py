'''
	Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

	Example 1:

	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.
	Example 2:

	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapping = {}
        squares = [num*num for num in range(1, int(pow(n, 0.5)) + 1)]
        for square in squares:
        	mapping[square] = 1

        for val in range(1, n+1):
        	if val not in mapping:
        		mapping[val] = float('inf')
        		for square in squares:
        			if square < val:
        				mapping[val] = min(mapping[val], mapping[square] + mapping[val-square])
        return mapping[n]
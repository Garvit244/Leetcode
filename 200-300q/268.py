'''
	Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

	Example 1:

	Input: [3,0,1]
	Output: 2
	Example 2:

	Input: [9,6,4,2,3,5,7,0,1]
	Output: 8
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        totalSum, n = sum(nums), len(nums)
        expectedSum = (n*(n+1))/2
        return expectedSum - totalSum
'''
	Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

	Example:

	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0

        currSum, result = nums[0], nums[0]

        for index in range(1, len(nums)):
        	currSum = max(nums[index], currSum+nums[index])
        	result = max(result, currSum)

        return result
'''
	Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

	Example:

	Input:  [1,2,3,4]
	Output: [24,12,8,6]
	 1 1 2 6
	 	12 8 6 
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
        	return []

        dp = [1]*len(nums)

        for index in range(1,len(nums)):
        	dp[index] = dp[index-1]*nums[index-1]
        print dp
        right = 1
        for index in range(len(nums)-1, -1, -1):
        	dp[index] *= right
        	right *= nums[index]
        return dp
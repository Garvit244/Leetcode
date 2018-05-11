'''
	Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

	Example 1:

	Input: [2,3,-2,4]
	Output: 6
	Explanation: [2,3] has the largest product 6.

	Example 2:

	Input: [-2,0,-1]
	Output: 0
	Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
        	return 0

        max_so_far, min_so_far, result = nums[0], nums[0], nums[0]

        for index in range(1, len(nums)):
        	if nums[index] > 0:
        		max_so_far = max(max_so_far*nums[index], nums[index])
        		min_so_far = min(min_so_far*nums[index], nums[index])
        	else:
        		temp = max_so_far
        		max_so_far = max(min_so_far*nums[index], nums[index])
        		min_so_far = min(temp*nums[index], nums[index])

        	result = max(result, max_so_far)
        return result
'''
	Given an unsorted array of integers, find the length of longest increasing subsequence.

	For example,
	Given [10, 9, 2, 5, 3, 7, 101, 18],
	The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

	Your algorithm should run in O(n2) complexity.

	Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
        	return len(nums)

        count = [0 for _ in range(len(nums))]
        result = 1
        count[0] = nums[0]

        for index in range(1, len(nums)):
        	if nums[index] < count[0]:
        		count[0] = nums[index]
        	elif nums[index] > count[result-1]:
        		count[result] = nums[index]
        		result += 1
        	else:
        		left, right = -1, result-1
        		while (right-left > 1):
        			mid = (left+right)/2
        			if count[mid] >= nums[index]:
        				right = mid
        			else:
        				left = mid
        		count[right] = nums[index]

        return result
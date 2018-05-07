'''
	Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

	Your algorithm's runtime complexity must be in the order of O(log n).

	If the target is not found in the array, return [-1, -1].

	Example 1:

	Input: nums = [5,7,7,8,8,10], target = 8
	Output: [3,4]
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1

        while left <= right:
        	mid = (left + right) /  2
        	if target > nums[mid]:
        		left = mid + 1
        	else:
        		right = mid

        if left == len(nums) or nums[left] != target:
        	return [-1, -1]

        result = [left]
        left, right = 0, len(nums) -1
        while left <= right:
        	mid = (left + right) / 2
        	if nums[mid] > target:
        		right = mid
        	else:
        		left = mid + 1

        result.append(left + 1)
        return result
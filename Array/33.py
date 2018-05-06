'''
	Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

	(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

	You are given a target value to search. If found in the array return its index, otherwise return -1.

	You may assume no duplicate exists in the array.

	Your algorithm's runtime complexity must be in the order of O(log n).
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
        	return -1

        left, right = 0, len(nums) - 1

        while left <= right:
        	mid = (left + right) / 2
        	if nums[mid] == target:
        		return mid

        	if nums[left] <= nums[mid]:
        		if target >= nums[left] and target <= nums[mid]:
        			right = mid - 1
        		else:
        			left = mid + 1
        	else:
        		if target >= nums[mid] and target <= nums[right]:
        			left = mid + 1
        		else:
        			right = mid - 1

        return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def searchRecursive(nums, left, right, target):
        	if left > right:
        		return -1

        	mid = (left + right) / 2
        	if nums[mid] == target:
        		return mid

        	if nums[left] <= nums[mid]:
        		if nums[left] <= target < nums[mid]:
        			return searchRecursive(nums, left, mid-1, target)
        		else:
        			return searchRecursive(nums, mid+1, right, target)
        	else:
        		if nums[mid] < target <= nums[right]:
        			return searchRecursive(nums, mid+1, right, target)
        		else:
        			return searchRecursive(nums, left, mid-1, target)

        return searchRecursive(nums, 0, len(nums)-1, target)
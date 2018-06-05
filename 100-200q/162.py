'''
	A peak element is an element that is greater than its neighbors.

	Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

	The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

	You may imagine that nums[-1] = nums[n] = -∞.

	Example 1:

	Input: nums = [1,2,3,1]
	Output: 2
	Explanation: 3 is a peak element and your function should return the index number 2.
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
        	mid = (left + right) /2
        	if nums[mid] > nums[mid+1]:
        		right = mid
        	else:
        		left = mid + 1
        return left


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [False]*len(nums)
        right = [False]*len(nums)
        left[0], right[len(nums)-1] = True, True

        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                left[index] = True

        for index in range(len(nums)-2, -1, -1):
            if nums[index] > nums[index+1]:
                right[index] = True

        for index in range(len(left)):
            if left[index] and right[index]:
                return index
        return -1
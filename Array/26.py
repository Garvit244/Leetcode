'''

	Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

	Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

	Example 1:

	Given nums = [1,1,2],

	Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

	It doesn't matter what you leave beyond the returned length.

'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        	
        index_i = 0

        for index_j in range(1, len(nums)):
        	if nums[index_i] != nums[index_j]:
        		index_i += 1
        		nums[index_i] = nums[index_j]

        return index_i + 1
'''
	Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

	Example:

	Input: [0,1,0,3,12]
	Output: [1,3,12,0,0]
	Note:

	You must do this in-place without making a copy of the array.
	Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroIndex = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[zeroIndex] = nums[index]
                zeroIndex += 1
                
        for index in range(zeroIndex, len(nums)):
            nums[index] = 0
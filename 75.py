'''
	Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

	Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

	Note: You are not suppose to use the library's sort function for this problem.

	Example:

	Input: [2,0,2,1,1,0]
	Output: [0,0,1,1,2,2]
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, last = 0, len(nums)-1
        index = 0
        while  index <= last:
        	if nums[index] == 1:
        		index += 1
        	elif nums[index] == 0:
        		nums[index], nums[zero] = nums[zero], nums[index]
        		index += 1
        		zero += 1
        	elif nums[index] == 2:
        		nums[last], nums[index] = nums[index], nums[last]
        		last -= 1
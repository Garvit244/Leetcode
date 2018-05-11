'''
	Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

	If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

	The replacement must be in-place and use only constant extra memory.

	Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

	1,2,3 → 1,3,2
	3,2,1 → 1,2,3
	1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index_i = len(nums) - 2
        while index_i >= 0 and nums[index_i] >= nums[index_i+1]:
        	index_i -= 1

        if index_i >= 0:
        	index_j = len(nums) - 1
        	while index_j >= index_i and nums[index_j] <= nums[index_i]:
        		index_j -= 1

        	nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
            
        start = index_i + 1
        end = len(nums) - 1
            
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
                
            
        
'''
	Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

	Note:

	The solution set must not contain duplicate triplets.

	Example:

	Given array nums = [-1, 0, 1, 2, -1, -4],

	A solution set is:
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        if (len(nums) >= 3) and (nums[0] == nums[len(nums) -1]) and (nums[0] == 0):
            return [[0, 0, 0]]

        result = []
        for index in range(len(nums) - 1):
        	left = index+1
        	right = len(nums) - 1

        	while left < right:
        		currSum = nums[index] + nums[left] + nums[right]
        		if currSum == 0:
        			result.append([nums[index], nums[left], nums[right]])
        			left += 1
        			right -= 1
        		elif currSum < 0:
        			left += 1
        		else:
        			right -= 1
        return  [list(t) for t in set(tuple(element) for element in result)]

# Space: O(1)
# Time: O(N^2)
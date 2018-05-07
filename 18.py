'''
	Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

	Note:

	The solution set must not contain duplicate quadruplets.

	Example:

	Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

	A solution set is:
	[
	  [-1,  0, 0, 1],
	  [-2, -1, 1, 2],
	  [-2,  0, 0, 2]
	]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        sumMapping = {}
        for index_i in range(len(nums)-1):
        	for index_j in range(index_i+1, len(nums)):
        		currSum = nums[index_i] + nums[index_j]
        		if currSum in sumMapping:
        			sumMapping[currSum].append((index_i, index_j))
        		else:
        			sumMapping[currSum] = [(index_i, index_j)]

        result = set()
        for key, value in sumMapping.iteritems():
        	diff = target - key
        	if diff in sumMapping:
        		firstSet = value
        		secondSet = sumMapping[diff]

        		for (i, j) in firstSet:
        			for (k, l) in secondSet:
        				fourlet = [i, j, k, l]
        				if len(set(fourlet)) != len(fourlet):
        					continue
        				fourlist = [nums[i], nums[j], nums[k], nums[l]]
        				fourlist.sort()
        				result.add(tuple(fourlist))

        return list(result)


# Space : O(N)
# Time: O(N^3)

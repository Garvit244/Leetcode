'''
	Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

		Note: The solution set must not contain duplicate subsets.

		Example:

		Input: [1,2,2]
		Output:
		[
		  [2],
		  [1],
		  [1,2,2],
		  [2,2],
		  [1,2],
		  []
		]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """   
        result = [[]]
        for num in nums:
        	for index in range(len(result)):
        		new_list = result[index] + [num]
        		new_list.sort()
        		result.append(new_list)
        unique = set(tuple(val) for val in result)
        return list(list(val) for val in unique)
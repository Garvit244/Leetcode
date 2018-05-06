'''
	Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

	Each number in candidates may only be used once in the combination.

	Note:

	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.
	Example 1:

	Input: candidates = [10,1,2,7,6,1,5], target = 8,
	A solution set is:
	[
	  [1, 7],
	  [1, 2, 5],
	  [2, 6],
	  [1, 1, 6]
	]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
        	if target < 0:
        		return
        	if target == 0:
        		result.append(currList)
        		return

        	previous = -1
        	for start in range(index, len(candidates)):
        		if previous != candidates[start]:
	        		recursive(candidates, target - candidates[start], currList + [candidates[start]], start+1)
	        		previous = candidates[start]


        recursive(candidates, target, [], 0)
        return result
'''
	Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

	The same repeated number may be chosen from candidates unlimited number of times.

	Note:

	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """  

        result = []

        def recursive(candidates, target, currList, index):
        	if target < 0:
        		return
        	if target == 0:
        		result.append(currList)
        		return

        	for start in range(index, len(candidates)):
        		recursive(candidates, target - candidates[start], currList + [candidates[start]], start)

        recursive(candidates, target, [], 0)
        return result

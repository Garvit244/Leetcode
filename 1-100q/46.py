class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
        	return []
        if len(nums) == 1:
        	return [nums]

        result = []
        for index in range(len(nums)):
        	for p in self.permute(nums[0:index] + nums[index+1:]):
        		result.append([nums[index]] + p)

        return result
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        nums = []
        for index in range(1, n+1):
        	nums.append(index)

        def permute(nums):
        	if len(nums) == 0:
        		return []
        	if len(nums) == 1:
        		return [nums]

        	result = []
        	for index in range(len(nums)):
        		for p in permute(nums[0:index] + nums[index+1:]):
        			result.append([nums[index]] + p)

        	return result

        value = permute(nums)[k-1]
        result = ""
        for val in value:
        	result += str(val)
        return result
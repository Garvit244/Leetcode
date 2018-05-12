'''
	Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

	Your algorithm should run in O(n) complexity.

	Example:

	Input: [100, 4, 200, 1, 3, 2]
	Output: 4
	Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums = set(nums)

        for num in nums:
        	if num-1 not in nums:
        		curr = num
        		length = 1

        		while curr+1 in nums:
        			curr += 1
        			length += 1
        		result = max(result, length)
        return result
'''
	Given a list of non negative integers, arrange them such that they form the largest number.

	Example 1:

	Input: [10,2]
	Output: "210"
	Example 2:

	Input: [3,30,34,5,9]
	Output: "9534330"
# '''


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
    	nums = [str(num) for num in nums]
    	nums.sort(cmp=lambda x, y : cmp(y+x, x+y))
    	return ''.join(nums).lstrip("0") or "0"
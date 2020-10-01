'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			diff = target - val
			if diff in mapping:
				return [index, mapping[diff]]
			else:
				mapping[val] = index
#Solution with the help of pointer
class Solution(object):
	def twoSum(self,nums,target):
		left=0
		right=len(nums)-1                       #sorted array so largest and smallest numbers
		while left<right:
			if nums[left]+nums[right]==target:
				print(nums[left],nums[right])
				return True
		        elif nums[left]+nums[right]>target:
				right-=1
			else:
				left+=1
		return False
				
				
				

				

# Space: O(N)
# Time: O(N)

'''
	Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

	Example 1:

	Input: [1,3,4,2,2]
	Output: 2
	Example 2:

	Input: [3,1,3,4,2]
	Output: 3
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[0]
        while True:
        	slow = nums[slow]
        	fast = nums[nums[fast]]
        	if slow == fast:
        		break

        num1= nums[0]
        num2 = slow
        while num1 != num2:
        	num1 = nums[num1]
        	num2 = nums[num2]
        return num2
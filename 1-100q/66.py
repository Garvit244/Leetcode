'''
	Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

	The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

	You may assume the integer does not contain any leading zero, except the number 0 itself.

	Example 1:

	Input: [1,2,3]
	Output: [1,2,4]
	Explanation: The array represents the integer 123
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        if not digits:
        	return []

        carry = 1
        new_digits = digits[::-1]

        for index in range(len(new_digits)):
        	new_digits[index], carry = (new_digits[index] + carry)%10, (new_digits[index] + carry)/10

        if carry > 0:
        	new_digits.append(carry)
        return new_digits[::-1]

Time: O(N)
Space: O(1)
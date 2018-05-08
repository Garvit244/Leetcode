'''
	Given two binary strings, return their sum (also a binary string).

	The input strings are both non-empty and contains only characters 1 or 0.

	Example 1:

	Input: a = "11", b = "1"
	Output: "100"

	Example 2:

	Input: a = "1010", b = "1011"
	Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        result = ""

        carry = 0
        index_a, index_b = len(a)-1, len(b)-1
        while index_a >= 0 and index_b >= 0:
        	result = (int(a[index_a]) + int(b[index_b]) + carry)%2 + result
        	carry = (int(a[index_a]) + int(b[index_b]) + carry)%2
        	index_a -= 1
        	index_b -= 1

        if index_a >= 0:
        	while index_a >= 0:
	        	result = (int(a[index_a]) + carry)%2 + result
	        	carry = (int(a[index_a]) + carry)%2
	        	index_a -= 1
	    elif index_b >= 0:
	    	while index_b >= 0:
	    		result = (int(b[index_b]) + carry)%2 + result
	    		carry = (int(b[index_b]) + carry)%2
	    		index_b -= 1
	    else:
	    	if carry == 1:
	    		result = str(carry) + result
	    return result
'''
	The count-and-say sequence is the sequence of integers with the first five terms as following:

	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221

	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.

	Given an integer n, generate the nth term of the count-and-say sequence. 
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
        	return "1"
        new_num = ""
        count_iter = 1
        num = "1"

        while count_iter < n:  
        	index_i, index_j = 0, 0
        	count, new_num = 0, ""

        	while index_j < len(num):
        		if num[index_i] != num[index_j]:
        			new_num += str(count) + str(num[index_i])
        			count = 0
        			index_i = index_j
        		else:
        			count += 1
        			index_j += 1

        	if count > 0:
        		new_num += str(count) + str(num[index_i])
        	num = new_num
        	count_iter += 1

        return new_num

# Space: O(1)
# Time: O(N*k) k= length of string
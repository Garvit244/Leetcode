'''
	Given a string s, partition s such that every substring of the partition is a palindrome.

	Return all possible palindrome partitioning of s.
'''

class Solution(object):
    def partition(self, s):
    	result = []
    	def valid(s):
    		for i in range(len(s)/2):
    			if s[i] != s[-(i+1)]:
    				return False
    		return True

    	def partitionRec(curr, s, i):
    		if i == len(s):
    			result.append(curr)
    		else:
    			for j in range(i, len(s)):
    				if valid(s[i:j+1]):
    					partitionRec(curr + [s[i:j+1]], s, j+1)

    	partitionRec([], s, 0)
    	return result
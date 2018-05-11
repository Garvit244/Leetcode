'''
	Given a string s, partition s such that every substring of the partition is a palindrome.

	Return the minimum cuts needed for a palindrome partitioning of s.

	Example:

	Input: "aab"
	Output: 1
	Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
        	return 0

        P = [[False for _ in range(len(s))] for _  in range(len(s))]
        cuts = [0 for _ in range(len(s))]

        for index in range(len(s)):
        	P[index][index] = True

        for length in range(2, len(s)+1):
        	for i in range(len(s)-length+1):
        		j = i+length - 1

        		if length == 2:
        			P[i][j] = s[i] == s[j]
        		else:
        			P[i][j] = (s[i] ==  s[j]) and P[i+1][j-1]

        for index in range(len(s)):
        	if P[0][index]:
        		cuts[index] = 0
        	else:
        		cuts[index] = float('inf')
        		for j in range(index):
        			if P[j+1][index] and (cuts[index] > 1 + cuts[j]):
        				cuts[index] = 1+cuts[j]

        return cuts[len(s)-1]

# Time: O(N^2)
# Space: O(N^2)        
'''
	You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

	Example 1:

	Input:
	  s = "barfoothefoobarman",
	  words = ["foo","bar"]
	Output: [0,9]
	Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
	The output order does not matter, returning [9,0] is fine too.
	Example 2:

	Input:
	  s = "wordgoodstudentgoodword",
	  words = ["word","student"]
	Output: []
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not str or not words:
        	return []

        counts = {}
        for word in words:
        	if word in counts:
        		counts[word] += 1
        	else:
        		counts[word] = 1

        result = []
        n, numOfWords, fixLen = len(s), len(words),len(words[0])

        for index in range(0, n-numOfWords*fixLen+1):
        	seen = {}

        	index_j = 0
        	while index_j < numOfWords:
        		word = s[index + index_j*fixLen: index + (index_j+1)*fixLen]
        		if word in counts:
        			if word in seen:
        				seen[word] += 1
        			else:
        				seen[word] = 1

        			if seen[word] > counts[word]:
        				break
        		else:
        			break
        		index_j += 1

        	if index_j == numOfWords:
        		result.append(index)

    	return 

# Time: O(N^2)
# Space: O(N)
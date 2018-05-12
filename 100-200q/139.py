'''
	Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

	Note:

	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
	Example 1:

	Input: s = "leetcode", wordDict = ["leet", "code"]
	Output: true
	Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for index in range(len(s)):
        	for j in range(i, -1, -1):
        		if dp[j] and s[j:i+1] in wordDict:
        			dp[i+1] = True
        			break
        return dp[len(s)]
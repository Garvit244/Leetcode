'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapSet = {}
        start, result = 0, 0

        for end in range(len(s)):
        	if s[end] in mapSet:
        		start = max(mapSet[s[end]], start)
        	result = max(result, end-start+1)
        	mapSet[s[end]] = end+1

        return result 


'''
Alternative solution
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        _set = set()
        ans = 0
        i, j = 0, 0
        
        while j < len(s):
            if s[j] not in _set:
                _set.add(s[j])
                j += 1
                ans = max(ans, len(_set))
            else:
                _set.remove(s[i])
                i += 1
                
        return ans

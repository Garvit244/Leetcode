'''
    Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

    Example 1:

    Input:
    s = "aaabb", k = 3

    Output:
    3

    The longest substring is "aaa", as 'a' is repeated 3 times.
    Example 2:

    Input:
    s = "ababbc", k = 2

    Output:
    5

    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1
        if all(dict[i] >= k for i in dict):
            return len(s)
        
        
        longest = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if dict[c] < k:
                longest = max(longest, self.longestSubstring(s[start:i], k))
                start = i + 1
                
        return max(longest, self.longestSubstring(s[start:], k))
				
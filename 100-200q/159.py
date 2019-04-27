'''
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''

class Solution(object):
	def lengthOfLongestSubstringTwoDistinct(self, s):
		"""
        :type s: str
        :rtype: int 
        """
        if not s:
        	return 0

        unique_char, start, result = {}, 0, 0
        for index, char in enumerate(s):
        	if char in unique_char:
        		unique_char[s] += 1
        	else:
        		unique_char[s] = 1

        	if len(unique_char) <= 2:
        		result = max(result, index-start+1)
        	else:
        		while len(unique_char) > 2:
        			char_index = s[start]
        			count = unique_char[char_index]
        			if count == 1:
        				del unique_char[char_index]
        			else:
        				unique_char[char_index] -= 1
        			start += 1
        return result

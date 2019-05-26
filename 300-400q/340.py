'''
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''

class Solution(object):
	def lengthOfLongestSubstringKDistinct(self, S, K):
		charMapping, start = {}, 0
		result = 0
		for end, s in enumerate(S):
			if s in charMapping:
				charMapping[s] += 1
			else:
				charMapping[s] = 1

			if len(charMapping) <= K:
				result = max(result, end-start+1)
			else:
				while len(charMapping) > K :
					character = S[start]
					freq = charMapping[character]
					if freq == 1:
						del charMapping[character]
					else:
						charMapping[character] -= 1
					start += 1
		return result

if __name__ == '__main__':
	print Solution().lengthOfLongestSubstringKDistinct("abcadcacacaca", 3)
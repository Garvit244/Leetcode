'''
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
'''

class Suffix(object):
	def __init__(self):
		self.index = 0
		self.first_rank = -1
		self.adjacent_rank = -1

	def __lt__(self, other):
		if self.first_rank == other.first_rank:
			return self.adjacent_rank < other.adjacent_rank
		return self.first_rank < other.first_rank
        
def create_suffix_array(s):
	N = len(s)
	suffix_array = []

	for index, char in enumerate(s):
		suffix_obj = Suffix()
		suffix_obj.index = index
		suffix_obj.first_rank = ord(char)-ord('a')
		suffix_obj.adjacent_rank = ord(s[index+1])-ord('a') if (index+1 < N) else -1
		suffix_array.append(suffix_obj)

	suffix_array.sort()

	no_char = 4
	index_map = {}
	while no_char < 2*N:
		rank = 0
		prev_rank, suffix_array[0].first_rank = suffix_array[0].first_rank, rank
		index_map[suffix_array[0].index] = 0

		for index in range(1, N):
			if suffix_array[index].first_rank == prev_rank and suffix_array[index].adjacent_rank == suffix_array[index-1].adjacent_rank:
				suffix_array[index].first_rank = rank
			else:
				rank += 1
				prev_rank, suffix_array[index].first_rank = suffix_array[index].first_rank, rank
			index_map[suffix_array[index].index] = index

		for index in range(N):
			adjacent_index = suffix_array[index].index + (no_char/2)
			suffix_array[index].adjacent_rank = suffix_array[index_map[adjacent_index]] if adjacent_index < N else -1

		suffix_array.sort()
		no_char *= 2    

	return [suffix.index for suffix in suffix_array]

def lcp_w_suffix_str(array, s):
	N = len(array)

	lcp_array = [0]*N
	inv_suffix = [0]*N

	for index in range(N):
		inv_suffix[array[index]] = index

	maxLen = 0

	for index in range(N):
		if inv_suffix[index] == N-1:
			maxLen = 0
			continue

		index_j = array[inv_suffix[index]+1]
		while(index+maxLen < N and index_j+maxLen < N and s[index+maxLen] == s[index_j+maxLen]):
			maxLen += 1

		lcp_array[inv_suffix[index]] = maxLen

		if maxLen > 0:
			maxLen -= 1

	return lcp_array

		
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        suffix_array = create_suffix_array(S)
        lcp_array = lcp_w_suffix_str(suffix_array, S)
        
        start, end = 0, 0
		
        for index in range(len(S)):
            if lcp_array[index] > end:
                end = lcp_array[index]
                start = suffix_array[index]
            
        if end == 0:
            return ""
        # print start, end
        return S[start:start+end]

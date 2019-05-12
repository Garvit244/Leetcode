from suffix_array import SuffixArray

class LCP(object):
	def __init__(self, s):
		self.s = s
		self.lcp_array = []
		self.suffix_array = SuffixArray(s)
		self.suffix_array.create_suffix_array()

	def lcp_w_suffix_str(self):
		N = len(self.suffix_array.suffix_array)
		array = self.suffix_array.suffix_array

		self.lcp_array = [0]*N
		inv_suffix = [0]*N

		for index in range(N):
			inv_suffix[array[index].index] = index

		maxLen = 0

		for index in range(N):
			if inv_suffix[index] == N-1:
				maxLen = 0
				continue

			index_j = array[inv_suffix[index]+1].index
			while(index+maxLen < N and index_j+maxLen < N and self.s[index+maxLen] == self.s[index_j+maxLen]):
				maxLen += 1

			self.lcp_array[inv_suffix[index]] = maxLen

			if maxLen > 0:
				maxLen -= 1

		return self.lcp_array


if __name__ == '__main__':
	lcp = LCP("banana")
	lcp.lcp_w_suffix_str()
	print lcp.lcp_array
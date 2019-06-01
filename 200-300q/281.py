'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''

class Solution(object):
	def __init__(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		self.index_v1 = 0
		self.index_v2 = 0

	def next(self):
		result = -1
		if self.index_v1 != len(self.v1) and self.index_v1 <= self.index_v2:
			result = self.v1[self.index_v1]
			self.index_v1 += 1
		else:
			result = self.v2[self.index_v2]
			self.index_v2 += 1

		return result

	def hasNext(self):
		return self.index_v1 < len(self.v1) or self.index_v2 < len(self.v2)


solution = Solution([1, 2], [3, 4, 5, 6])
while solution.hasNext():
	print solution.next()
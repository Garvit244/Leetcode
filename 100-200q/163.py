'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''

class Solution(object):
	def missingRange(self, A, lower, upper):
		if not A:
			return []

		result = []
		if A[0] != lower:
			end = A[0] - 1
			if end == lower:
				m_r = str(lower)
			else:
				m_r = str(lower) + "->" + str(end)
			result.append(m_r)

		for index in range(1, len(A)):
			if A[index] != A[index-1] + 1:
				start = A[index-1] + 1
				end = A[index] - 1
				if start == end:
					m_r = str(start)
				else:
					m_r = str(start) + "->" + str(end)
				result.append(m_r)

		if A[len(A) - 1] != upper:
			start = A[len(A)-1] + 1
			if start == upper:
				m_r = str(start)
			else:
				m_r = str(start) + "->" + str(upper)
			result.append(m_r)
		return result

solution = Solution()
print solution.missingRange([0, 1, 3, 50, 75], 0, 99)
print solution.missingRange([4, 10, 50, 98], 0, 99)
print solution.missingRange([0], 0, 1)
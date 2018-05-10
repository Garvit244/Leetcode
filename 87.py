'''
	Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

	Below is one possible representation of s1 = "great":

	    great
	   /    \
	  gr    eat
	 / \    /  \
	g   r  e   at
	           / \
	          a   t

	To scramble the string, we may choose any non-leaf node and swap its two children.

	For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

	    rgeat
	   /    \
	  rg    eat
	 / \    /  \
	r   g  e   at
	           / \
	          a   t

	We say that "rgeat" is a scrambled string of "great".
'''

class Solution(object):
	def __init__(self):
		self.cache = {}

	def isScramble(self, s1, s2):
		if s1 == s2:
			return True
		if s1+s2 in self.cache:
			return self.cache[s1+s2]
		if len(s1) != len(s2) or sorted(s1) != sorted(s2):
			self.cache[s1+s2] = False
			return False
		for index in range(1, len(s1)):
			if self.isScramble(s1[:index], s2[:index]) and self.isScramble(s1[index:], s2[index:]):
				self.cache[s1+s2] =True
				return True
			if self.isScramble(s1[:index], s2[-index:]) and self.isScramble(s1[index:], s2[0:-index]):
				self.cache[s1+s2] = True
				return True

		self.cache[s1+s2] =False
		return False  		
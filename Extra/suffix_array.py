class Suffix(object):
	def __init__(self):
		self.index = 0
		self.first_rank = -1
		self.adjacent_rank = -1

	def __lt__(self, other):
		if self.first_rank == other.first_rank:
			return self.adjacent_rank < other.adjacent_rank
		return self.first_rank < other.first_rank

class SuffixArray(object):
	def __init__(self, s):
		self.s = s
		self.suffix_array = []

	def print_suffix(self):
		for index in range(len(self.s)):
			ele = self.suffix_array[index]
			print("Suffix index {}, Suffix string {}".format(ele.index, self.s[ele.index:]))

	def create_suffix_array(self):
		N = len(self.s)
		
		for index, char in enumerate(self.s):
			suffix_obj = Suffix()
			suffix_obj.index = index
			suffix_obj.first_rank = ord(char)-ord('a')
			suffix_obj.adjacent_rank = ord(self.s[index+1])-ord('a') if (index+1 < N) else -1
			self.suffix_array.append(suffix_obj)

		self.suffix_array.sort()

		no_char = 4
		index_map = {}
		while no_char < 2*N:
			rank = 0
			prev_rank, self.suffix_array[0].first_rank = self.suffix_array[0].first_rank, rank
			index_map[self.suffix_array[0].index] = 0

			for index in range(1, N):
				if self.suffix_array[index].first_rank == prev_rank and self.suffix_array[index].adjacent_rank == self.suffix_array[index-1].adjacent_rank:
					self.suffix_array[index].first_rank = rank
				else:
					rank += 1
					prev_rank, self.suffix_array[index].first_rank = self.suffix_array[index].first_rank, rank
				index_map[self.suffix_array[index].index] = index

			for index in range(N):
				adjacent_index = self.suffix_array[index].index + (no_char/2)
				self.suffix_array[index].adjacent_rank = self.suffix_array[index_map[adjacent_index]] if adjacent_index < N else -1

			self.suffix_array.sort()
			no_char *= 2

if __name__ == '__main__':
	suffix_array = SuffixArray("banana")
	suffix_array.create_suffix_array()
	suffix_array.print_suffix()
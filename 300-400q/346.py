'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class Solution(object):
	def __init__(self):
		self.queue = []
		self.curr_sum = 0

	def movingAverage(self, num, size):
		if len(self.queue) >= size:
			val = self.queue.pop(0)
			self.curr_sum -= val

		self.curr_sum += num
		self.queue.append(num)
		return float(self.curr_sum)/len(self.queue)

	

solution = Solution()
window_size = int(input())
num = int(input())
while num != -1:
	print solution.movingAverage(num, window_size)
	num = int(input())
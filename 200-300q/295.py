'''
	Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

	Examples: 
	[2,3,4] , the median is 3

	[2,3], the median is (2 + 3) / 2 = 2.5

	Design a data structure that supports the following two operations:

	void addNum(int num) - Add a integer number from the data stream to the data structure.
	double findMedian() - Return the median of all elements so far.
	For example:

	addNum(1)
	addNum(2)
	findMedian() -> 1.5
	addNum(3) 
	findMedian() -> 2
'''
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.max_heap or num > -self.max_heap[0]:
        	heapq.heappush(self.min_heap, num)

        	if len(self.min_heap) > len(self.max_heap) + 1:
        		heapq.heappush(self.max_heap, -heapq.heapop(self.min_heap))
		else:
			heapq.heappush(self.max_heap, -num)
			if len(self.max_heap) > len(self.min_heap):
				heapq.heappush(self.min_heap, -heapq.heapop(self.max_heap))        

    def findMedian(self):
        """
        :rtype: float
        """
        print self.max_heap, self.min_heap
        if len(self.max_heap) == len(self.min_heap):
        	return (-self.max_heap[0]+self.min_heap[0] )/2.0
        else:
        	return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 
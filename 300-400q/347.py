'''
	Given a non-empty array of integers, return the k most frequent elements.

	For example,
	Given [1,1,1,2,2,3] and k = 2, return [1,2]
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
        	return []
        frequency = {}
        for num in nums:
        	if num in frequency:
        		frequency[num] += 1
        	else:
        		frequency[num] = 1

       	result = []
       	import heapq
       	heap = []

       	for key, value in frequency.iteritems():
       		heapq.heappush(heap, (-value, key))

       	for _ in range(k):
       		result.append(heapq.heappop(heap)[1])
       	return result
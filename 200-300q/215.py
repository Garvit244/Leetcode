'''
	Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

	Example 1:

	Input: [3,2,1,5,6,4] and k = 2
	Output: 5
	Example 2:

	Input: [3,2,3,1,2,4,5,5,6] and k = 4
	Output: 4
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        import heapq
        for num in nums:
        	heapq.heappush(heap, -(num))

        result = 0
        for _ in range(k):
        	result = heapq.heappop(heap)

        return -(result)

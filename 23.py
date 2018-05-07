'''
	Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

	Example:

	Input:
	[
	  1->4->5,
	  1->3->4,
	  2->6
	]
	Output: 1->1->2->3->4->4->5->6

'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        from heapq import heappush, heappop

        heap = []
        head = point = ListNode(0)
        for element in lists:
        	if element:
        		heapq.heappush(heap, (element.val, element))

        while heap:
        	value, node = heapq.heappop(heap)
        	head.next = ListNode(value)
        	head = head.next
        	node = node.next
        	if node:
        		heapq.heappush(heap, (node.val, node))

        return point.next

# Space: O(K)
# Time: O(N*log(K))

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge2Lists(l1, l2):
        	head = point = ListNode(0)
        	while l1 and l2:
        		if l1.val <= l2.val:
        			point.next = ListNode(l1.val)
        			l1 = l1.next
        		else:
        			point.next = ListNode(l2.val)
        			l2 = l2.next
        		point = point.next

        	if l1:
        		point.next = l1
        	else:
        		point.next = l2
        	return head.next

        if not lists:
        	return lists

        interval = 1
        while interval < len(lists):
        	for index in range(0, len(lists) - interval ,interval*2):
        		lists[index] = merge2Lists(lists[index], lists[index+interval])

        	interval *= 2

        return lists[0]



# Time: O(N*log(k))
# Space: O(1)
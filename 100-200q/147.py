# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
        	return None

        sortedList = head
        head = head.next
        sortedList.next = None

        while head:
        	curr = head
        	head = head.next
        	if curr.val <= sortedList.val:
        		curr.next = sortedList
        		sortedList = curr
        	else:
        		temp = sortedList
        		while temp.next and temp.next.val < curr.val:
        			temp = temp.next
        		curr.next = temp.next
        		temp.next = curr
        return sortedList
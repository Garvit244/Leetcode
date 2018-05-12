'''
	Reverse a singly linked list.

	Example:

	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return None

        prev, curr = None, head
        while curr:
        	temp = curr.next
        	curr.next = prev
        	prev = curr
        	curr = temp
        return prev
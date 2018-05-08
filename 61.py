# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
        	return head
        if not head:
        	return None

        tempHead, length = head, 1
        while tempHead.next:
        	length += 1
        	tempHead = tempHead.next

        tempHead.next = head
        jump = (length-k)%length

        previous = tempHead
        while jump > 0:
        	previous = previous.next
        	jump -= 1
        head = previous.next
        previous.next = None

        return head
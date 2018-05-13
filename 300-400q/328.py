'''
	Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

	You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

	Example:
	Given 1->2->3->4->5->NULL,
	return 1->3->5->2->4->NULL.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if  not head:
        	return None

        odd, even = head, head.next
        evenHead = even
        while even and even.next:
        	odd.next = even.next
        	odd = odd.next
        	even.next = odd.next
        	even = even.next

        odd.next = evenHead
        return head
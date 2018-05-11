'''
	Reverse a linked list from position m to n. Do it in one-pass.

	Note: 1 ≤ m ≤ n ≤ length of list.

	Example:

	Input: 1->2->3->4->5->NULL, m = 2, n = 4
	Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n :
        	return head

        result = ListNode(0)
        result.next = head

        prev = result

        for index in range(m-1):
        	prev = prev.next

        reverse = None
        curr = prev.next
        for i in range(n-m+1):
        	temp = curr.next
        	curr.next = reverse
        	reverse = curr
        	curr = temp

        prev.next.next = curr
        prev.next = reverse
        return result.next
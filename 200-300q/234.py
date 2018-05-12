# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow, fast = head, head.next
        while fast and fast.next:
        	fast = fast.next.next
        	temp = slow
        	slow = slow.next
        	temp.next = rev
        	rev = temp

        if fast:
        	slow = slow.next

        while rev and rev.val == slow.val:
        	rev = rev.next
        	slow = slow.next
        return not rev
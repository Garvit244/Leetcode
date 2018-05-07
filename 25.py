'''
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

    Example:

    Given this linked list: 1->2->3->4->5

    For k = 2, you should return: 2->1->4->3->5

    For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if head:
            slow = head # the mover
            while slow:
                group = []
                while slow and len(group) < k:
                    group.append(slow)
                    slow = slow.next
                    if not slow and len(group) < k:
                        return head
                for i in range(k/2):
                    print i,k-i-1
                    group[i].val,group[k-i-1].val = group[k-i-1].val,group[i].val
        return head

# Space: O(k)
# Time: O(N)
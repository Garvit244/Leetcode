'''
	Given two binary trees, write a function to check if they are the same or not.

	Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

	Example 1:

	Input:     1         1
	          / \       / \
	         2   3     2   3

	        [1,2,3],   [1,2,3]

	Output: true
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
        	return True 

        stack = [(p, q)]

        while stack:
        	node1, node2 = stack.pop()
        	if node1 and node2 and node1.val == node2.val:
        		stack.append((node1.left, node2.left))
        		stack.append((node1.right, node2.right))
        	else:
        		if not node1 == node2:
        			return False 

        return True
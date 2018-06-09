'''
	Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
	Note: If the given node has no in-order successor in the tree, return null
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
		"""

		if not root or not p:
			return None

		if p.right:
			p = p.right
			while p.left:
				p = p.left
			return p

		successor = None
		while root and root != p:
			if root.val > p.val:
				successor = root
				root = root.left
			else:
				root = root.right
		return successor
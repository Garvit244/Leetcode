'''
	Given a binary tree, find its minimum depth.

	The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

	Note: A leaf is a node with no children.

	Example:

	Given binary tree [3,9,20,null,null,15,7],

	    3
	   / \
	  9  20
	    /  \
	   15   7

	return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
    	if not root:
    		return 0
    	depth = float('inf')
    	stack = [(root, 1)]

    	while stack:
    		node, level = stack.pop()
    		if node:

    			if not node.left and not node.right:
    				depth = min(depth, level)

    			stack.append((node.left, level+1))
    			stack.append((node.right, level+1))

    	return depth
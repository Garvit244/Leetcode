'''
	Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

	Example:

	Input: [1,2,3,null,5,null,4]
	Output: [1, 3, 4]
	Explanation:

	   1            <---
	 /   \
	2     3         <---
	 \     \
	  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []

        stack, node_depth = [(root, 0)], {}

        while stack:
        	node, depth = stack.pop(0)
        	if depth not in node_depth:
        		node_depth[depth] = node.val

        	if node.right:
        		stack.append((node.right, depth+1))
        	if node.left:
        		stack.append((node.left, depth+1))
        return node_depth.values()
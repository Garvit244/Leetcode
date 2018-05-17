'''
	Given a binary tree, return the postorder traversal of its nodes' values.

	Example:

	Input: [1,null,2,3]
	   1
	    \
	     2
	    /
	   3

	Output: [3,2,1]
	Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []

        def recursive(root, result):
        	if not root:
        		return
        	recursive(root.left, result)
        	recursive(root.right, result)
        	result.append(root.val)
        recursive(root, result)
        return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
        	return []

        stack, result = [], []

        while True:
        	while root:
        		if root.right:
        			stack.append(root.right)
        		stack.append(root)
        		root = root.left

        	root = stack.pop()

        	if root.right and stack and stack[-1] == root.right:
        		stack.pop()
        		stack.append(root)
        		root = root.right
        	else:
        		result.append(root.val)
        		root = None

        	if  len(stack)<=0:
        		break

        return result
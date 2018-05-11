'''
	Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

	For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

	    1
	   / \
	  2   2
	 / \ / \
	3  4 4  3

	But the following [1,2,2,null,3,null,3] is not:

	    1
	   / \
	  2   2
	   \   \
	   3    3

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True

        def dfs(left, right):
        	if not left and not right:
        		return True

        	if not left or not right:
        		return False
        	return (left.val == right.val) and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)
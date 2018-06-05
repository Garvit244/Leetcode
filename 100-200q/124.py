'''
	Given a non-empty binary tree, find the maximum path sum.

	For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

	Example 1:

	Input: [1,2,3]

	       1
	      / \
	     2   3

	Output: 6
	Example 2:

	Input: [-10,9,20,null,null,15,7]

	   -10
	   / \
	  9  20
	    /  \
	   15   7

	Output: 42
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('-inf')
        self.dfs(root)
        return self.result

    def dfs(self, root):
    	if not root:
    		return 0

    	l = self.dfs(root.left)
    	r = self.dfs(root.right)

    	max_one_end = max(max(l, r)+root.val, root.val)
    	max_path = max(max_one_end, l+r+root.val)
    	self.result = max(self.result, max_path)
    	return max_one_end



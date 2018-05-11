'''
	Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

	Note: A leaf is a node with no children.

	Example:

	Given the below binary tree and sum = 22,

	      5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \    / \
	7    2  5   1
	Return:

	[
	   [5,4,11,2],
	   [5,8,4,5]
	]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        result = []

        def dfs(root, curr_sum, sum, path, result):
        	if not root:
        		return

        	curr_sum += root.val
        	if curr_sum == sum and not root.left and not root.right:
        		result.append(path + [root.val])
        		return

        	if root.left:
        		dfs(root.left, curr_sum, sum, path + [root.val], result)
        	if root.right:
        		dfs(root.right, curr_sum, sum, path + [root.val], result)

        dfs(root, 0, sum, [], result)
        return result
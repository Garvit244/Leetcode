'''
	Given a binary tree, return all root-to-leaf paths.

	Note: A leaf is a node with no children.

	Example:

	Input:

	   1
	 /   \
	2     3
	 \
	  5

	Output: ["1->2->5", "1->3"]

	Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        def dfs(root, curr):
            if root.left is None and root.right is None:
                paths.append(curr + str(root.val))
                return
                
            if root.left:
                dfs(root.left, curr + str(root.val) + '->')
            if root.right:
                dfs(root.right, curr + str(root.val) + '->')
            
        curr = ""
        dfs(root, curr)
        return paths
'''
	Given inorder and postorder traversal of a tree, construct the binary tree.

	Note:
	You may assume that duplicates do not exist in the tree.

	For example, given

	inorder = [9,3,15,20,7]
	postorder = [9,15,7,20,3]
	Return the following binary tree:

	    3
	   / \
	  9  20
	    /  \
	   15   7
 '''

 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.index = len(inorder)-1
        def recursive(postorder, inorder, start, end):
        	if start > end:
        		return None

        	node = TreeNode(postorder[self.index])
        	self.index -= 1
        	if start == end:
        		return node

        	search_index = 0
        	for i in range(start, end+1):
        		if inorder[i] == node.val:
        			search_index = i
        			break
        	node.right = recursive(postorder, inorder, search_index+1, end)
        	node.left = recursive(postorder, inorder, start, search_index-1)
        	return node

        return recursive(postorder, inorder, 0, len(inorder)-1)
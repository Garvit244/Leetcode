'''
	Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

	Note:

	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
	Example 1:

	Input: s = "leetcode", wordDict = ["leet", "code"]
	Output: true
	Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.index = 0
        def recursive(preorder, inorder, start, end):
        	if start > end:
        		return None

        	node = TreeNode(preorder[self.index])
        	self.index += 1
        	if start == end:
        		return node

        	search_index = 0
        	for i in range(start, end+1):
        		if inorder[i] == node.val:
        			search_index = i
        			break

        	node.left = recursive(preorder, inorder, start, search_index-1)
        	node.right = recursive(preorder, inorder, search_index+1, end)
        	return node

        return recursive(preorder, inorder, 0, len(inorder)-1)
'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''


class Solution(object):
	def dfs(curr, parent, length):
		if not curr:
			return length
		if parent:
			length = length + 1 if curr.val == parent.val + 1
		else:
			length = 1

		return max(length, max(dfs(curr.left, curr, length), dfs(curr.right, curr, length)))

	def longestConsecutive(TreeNode root):
		if not root:
			return 0

		return dfs(root, null, 0)

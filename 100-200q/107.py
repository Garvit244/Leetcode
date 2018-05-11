'''
    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

    return its bottom-up level order traversal as:

    [
      [15,7],
      [9,20],
      [3]
    ]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
        	return []

        queue = [(root, 0)]
        levelMap = {}

        while queue:
        	node, level = queue.pop(0)
        	if node.left:
        		queue.append((node.left, level+1))
        	if node.right:
        		queue.append((node.right, level+1))

        	if level in levelMap:
        		levelMap[level].append(node.val)
        	else:
        		levelMap[level] = [node.val]

        result = []
        for key, value in levelMap.iteritems():
        	result.append(value)
        return result[::-1]
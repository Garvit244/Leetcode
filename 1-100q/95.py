'''
	Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

	Example:

	Input: 3
	Output:
	[
	  [1,null,3,2],
	  [3,2,null,1],
	  [3,1,null,null,2],
	  [2,1,3],
	  [1,null,2,null,3]
	]
	Explanation:
	The above output corresponds to the 5 unique BST's shown below:

	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
        	return []


        def generate(start, end):
        	result = []
        	if start > end:
        		result.append(None)
        		return result

        	for index in range(start, end+1):
        		left = generate(start, index-1)
        		right = generate(index+1, end)

        		for l in left:
        			for r in right:
        				current = TreeNode(index)
        				current.left = l
        				current.right = r
        				result.append(current)

        	return result

        return generate(1, n)
'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def adjacent(self, root, node1, node2):
            if not root:
                return False
            
            value = False
            if (root.right and root.left):
                value = ((root.left.val == node1 and root.right.val == node2) or 
                         (root.left.val == node2 and root.right.val == node1))
                
            return (value or
                   self.adjacent(root.left, node1, node2) or
                   self.adjacent(root.right, node1, node2))
        
    def _level(self, root, node, level):
            if not root:
                return 0
            if root.val == node:
                return level
            
            left_level = self._level(root.left, node, level+1)
            if left_level != 0:
                return left_level
            return self._level(root.right, node, level+1)
        
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if ((self._level(root, x, 1) == self._level(root, y, 1)) and not self.adjacent(root, x, y)):
            return True
        return False

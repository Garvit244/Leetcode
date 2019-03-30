'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for index in range(1, len(preorder)):
            new_node = TreeNode(preorder[index])
            if new_node.val < stack[-1].val:
                stack[-1].left = new_node
            else:
                parent = None
                while stack and new_node.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = new_node
            stack.append(new_node)
        return root
        
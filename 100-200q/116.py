'''
	Given a binary tree

	struct TreeLinkNode {
	  TreeLinkNode *left;
	  TreeLinkNode *right;
	  TreeLinkNode *next;
	}
	Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

	Initially, all next pointers are set to NULL
	Example:

	Given the following perfect binary tree,

	     1
	   /  \
	  2    3
	 / \  / \
	4  5  6  7
	After calling your function, the tree should look like:

	     1 -> NULL
	   /  \
	  2 -> 3 -> NULL
	 / \  / \
	4->5->6->7 -> NULL
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def recursive(node):
        	if node is None:
        		return

        	if node.left:
        		node.left.next = node.right
        	if node.right:
        		if node.next:
	        		node.right.next = node.next.left
	        	else:
	        		node.right.next  = None
	        recursive(node.left)
	        recursive(node.right)

		if root != None:
			root.next = None
			recursive(root)
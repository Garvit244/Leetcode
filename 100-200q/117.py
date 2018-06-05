'''
	Given a binary tree

	struct TreeLinkNode {
	  TreeLinkNode *left;
	  TreeLinkNode *right;
	  TreeLinkNode *next;
	}
	Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

	Initially, all next pointers are set to NULL.

	Example:

	Given the following binary tree,

	     1
	   /  \
	  2    3
	 / \    \
	4   5    7
	After calling your function, the tree should look like:

	     1 -> NULL
	   /  \
	  2 -> 3 -> NULL
	 / \    \
	4-> 5 -> 7 -> NULL
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
    	if root == None:
    		return 
    	queue = [root]
    	queue.append(None)

    	while queue:
    		front = queue.pop(0)
    		if front is not None:
    			front.next = queue[0]
    			if front.left:
    				queue.append(front.left)
    			if front.right:
    				queue.append(front.right)
    		elif queue:
    			queue.append(None)


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
    	if not root:
    		return None

    	root.next = None

    	while root:
    		temp = root
    		while temp:
    			if temp.left:
    				if temp.right:
    					temp.left.next = temp.right
    				else:
    					temp.left.next = self.getNext(temp)
    			if temp.right:
    				temp.right.next = self.getNext(temp)

    			temp = temp.next
    		if root.left:
    			root = root.left
    		elif root.right:
    			root = root.right
    		else:
    			root = self.getNext(root)

    def getNext(self, node):
    	node = node.next
    	while node:
    		if node.left:
    			return node.left
    		if node.right:
    			return node.right
    		node = node.next
    	return None
'''
	Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

	Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

	Example: 

	You may serialize the following tree:

	    1
	   / \
	  2   3
	     / \
	    4   5

	as "[1,2,3,null,null,4,5]"
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(root):
            if root:
                seralizeTree.append(str(root.val) + ',')
                preorder(root.left)
                preorder(root.right)
            else:
                seralizeTree.append('#,')
                
        seralizeTree = []
        preorder(root)
        return ''.join(seralizeTree)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def buildTree(preorder):
            value = preorder.pop(0)
            if value == '#':
                return None
            
            node = TreeNode(int(value))
            node.left = buildTree(preorder)
            node.right = buildTree(preorder)
            return node
            
        preorder = data.split(',')[:-1]
        return buildTree(preorder)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
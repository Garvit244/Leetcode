'''
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)


Example 1:
	    8
	  /   \
	3	   10
  /	  \      \
1	   6	  14
	  /  \    /
	4	  7	 13

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def utility_fun(root, res):
            if not root:
                return 2147483648, -2147483648, res
            if not root.left and not root.right:
                return root.val, root.val, res
            left_t, lmax_t, res = utility_fun(root.left, res)
            right_t, rmax_t, res = utility_fun(root.right, res)
            m_val = min(left_t, right_t)
            max_val = max(lmax_t, rmax_t)
                
            res = max(res, max(abs(root.val-m_val), abs(root.val-max_val)))
            # print res
            return min(m_val, root.val), max(max_val, root.val), res
        
        x, x2, res = utility_fun(root, -2147483648)
        return abs(res)

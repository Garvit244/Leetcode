'''
    You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

    Example:

    Given nums = [5, 2, 6, 1]

    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    Return the array [2, 1, 1, 0].
'''

class TreeNode(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val
        self.count = 1
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        
        node = TreeNode(nums[len(nums)-1])
        result = [0]
        for index in range(len(nums)-2, -1, -1):
            result.append(self.insertNode(node, nums[index]))
            
        return result[::-1]
    
    def insertNode(self, node, val):
        totalCount = 0
        while True:
            if val <= node.val:
                node.count += 1
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                totalCount += node.count
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
                    
        return totalCount
                
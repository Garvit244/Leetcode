'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class Node(object):
    def __init__(self, val ,start, end):
        self.sum = val
        self.right, self.left = None, None
        self.range= [start, end]
        
class SegementTree(object):
    def __init__(self, size):
        self.root = self._build_segment_tree(0, size-1)
        
    def _build_segment_tree(self, start, end):
        if start > end:
            return None
        node = Node(0, start, end)
        if start == end:
            return node
        mid = (start+end)/2
        node.left, node.right = self._build_segment_tree(start, mid), self._build_segment_tree(mid+1, end)
        return node
    
    def update(self, index, val, root=None):
        root = root or self.root
        if index < root.range[0] or index > root.range[1]:
            return
        root.sum += val
        if index == root.range[0] == root.range[1]:
            return 
        self.update(index, val, root.left)
        self.update(index, val, root.right)
            
    def range_sum(self, start, end, root=None):
        root = root or self.root
        if end < root.range[0] or start > root.range[1]:
            return 0
        if start <= root.range[0] and end >= root.range[1]:
            return root.sum
        return self.range_sum(start, end, root.left) + self.range_sum(start, end, root.right)
        
        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.segment_tree = SegementTree(len(nums))
        for index, num in enumerate(nums):
            self.segment_tree.update(index, num)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val-self.nums[i]
        self.segment_tree.update(i, diff)
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.segment_tree.range_sum(i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
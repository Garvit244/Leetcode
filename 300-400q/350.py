'''
	Given two arrays, write a function to compute their intersection.

	Example:
	Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

	Note:
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.
	Follow up:
	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1's size is small compared to nums2's size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1.sort()
        nums2.sort()

        index_i, index_j = 0, 0
        result = []
        while index_i < len(nums1) and index_j < len(nums2):
        	if nums1[index_i] == nums2[index_j]:
        		result.append(nums1[index_i])
        		index_i += 1
        		index_j += 1
        	elif nums1[index_i] > nums2[index_j]:
        		index_j += 1
        	else:
        		index_i += 1
        return result
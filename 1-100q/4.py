'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.

	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]

	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]

	The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
        	nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low , high = 0, x

        while  low <= high:
        	partitionx = (low+high)/2
        	partitiony = (x+y+1)/2 - partitionx
        	if partitionx == 0:
        		maxLeftX = float('-inf')
        	else:
	        	maxLeftX = nums1[partitionx-1]

	        if partitionx == x:
	        	minRightX = float('inf')
	        else:
	        	minRightX = nums1[partitionx]

	        if partitiony == 0:
	        	maxLeftY = float('-inf')
	        else:
	        	maxLeftY = nums2[partitiony-1]

	        if partitiony == y:
	        	minRightY = float('inf')
	        else:
	        	minRightY = nums2[partitiony]

	        if maxLeftX <= minRightY and maxLeftY <= minRightX:
	        	if((x+y)%2 == 0):
	        		return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
	        	else:
	        		return max(maxLeftY, maxLeftX)
	        elif maxLeftX > minRightY:
	        	high = partitionx - 1
	        else:
	        	low = partitionx + 1


print Solution().findMedianSortedArrays([1,2], [3, 4])
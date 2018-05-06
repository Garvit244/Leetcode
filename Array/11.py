'''
	Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

	Note: You may not slant the container and n is at least 2.

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxArea = 0, len(height) - 1, 0 

        while left < right:
        	maxArea = max(maxArea, min(height[left], height[right])*(right-left))
        	if height[left] < height[right]:
        		left += 1
        	else:
        		right -= 1

        return maxArea 

# Space : O(1)
# Time: O(N)
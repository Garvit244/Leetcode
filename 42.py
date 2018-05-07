'''
	Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        result = 0
        while left < right:
        	if height[left] < height[right]:
        		if height[left] > leftMax:
        			leftMax = height[left]
        		else:
        			result += (leftMax - height[left])
        		left += 1
        	else:
        		if height[right] > rightMax:
        			rightMax = height[right]
        		else:
        			result += (rightMax - height[right])
        		right -= 1

        return result 
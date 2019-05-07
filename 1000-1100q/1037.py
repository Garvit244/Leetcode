'''
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
'''

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1, x2, x3, y1, y2, y3 = points[0][0], points[1][0], points[2][0], points[0][1], points[1][1] ,points[2][1]
        if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)):
            return False
        return True

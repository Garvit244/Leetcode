'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
'''

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) != len(B):
            return -1
        if len(A) == 0:
            return 0
        
        for possibility in set([A[0], B[0]]):
            top_rotation, bottom_rotation =0, 0
            for a_num, b_num in zip(A, B):
                if possibility not in [a_num, b_num]:
                    break
                top_rotation += int(b_num != possibility)
                bottom_rotation += int(a_num != possibility)
            else:
                return min(top_rotation, bottom_rotation)
        return -1
 
'''
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

 

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 

Note:

1 <= N <= 10^9
'''

class Solution(object):
    result = 0
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        original_a = [0, 1, 6, 8, 9]
        o_rotation = [0, 1, 9, 8, 6]
        
        def recursive(original, rotation, digit, N):
            if original > N:
                return
            if original and original != rotation:
                self.result += 1
            
            start = original == 0
            if digit >= 1000000000:
                return
            for index in range(start, 5):
                recursive(original * 10 + original_a[index], rotation + o_rotation[index]*digit, digit*10, N)
            
        recursive(0, 0, 1, N)
        if (N == 1000000000):
            self.result += 1
        return self.result

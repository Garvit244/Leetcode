'''
Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
'''

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for num in range(1, N+1):
            binary_str = ''
            while (num != 0):
                binary_str += str(num%2)
                num /= 2
            reversed_str = binary_str[::-1]
            
            if reversed_str not in S:
                return False
        return True
 
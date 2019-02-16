'''
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
'''

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        
        result = ''
        if A > B:
            while B > 0 and A > 0:
                if A-B >= 3:
                    if A > 1:
                        result += 'aab'
                        A -= 2
                    else:
                        result += 'ab'
                        A -= 1
                    B -= 1
                else:
                    result += 'ab'
                    A -= 1
                    B -= 1
            if A > 0:
                result += 'a'*A
            if B > 0:
                result += 'b'*B
        else:
            while B > 0 and A > 0:
                if B-A >= 3:
                    if B > 1:
                        result += 'bba'
                        B -= 2
                    else:
                        result += 'ba'
                        B -= 1
                    A -= 1
                else:
                    result += 'ba'
                    A -= 1
                    B -= 1
            if A > 0:
                result += 'a'*A
            if B > 0:
                result += 'b'*B
                
        return result

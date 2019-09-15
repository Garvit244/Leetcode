'''
Given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

 
Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
'''

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        stack = []
        for char in s:
            if char == ')':
                combine_str = ''
                while stack and stack[-1] != '(':
                    elem = stack.pop()[::-1]
                    combine_str += elem
                stack.pop()
                stack.append(combine_str)
            else:
                stack.append(char)
        return "".join(stack)

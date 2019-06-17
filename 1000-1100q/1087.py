'''
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

 

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
 

Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
'''

class Solution(object):
    def permute(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        if not S:
            return []
        if '{' not in S:
            return [S]
        stack, stack2 = [], []
        brace = 0
        for char in S:
            if char == '{':
                brace = 1
            elif char == '}':
                if not stack:
                    stack = stack2
                else:
                    new_stack = []
                    for char in stack:
                        for char2 in stack2:
                            new_stack.append(char + char2)
                                
                    stack = new_stack
                stack2 = []
                brace = 2
            elif char != ',':
                if brace == 1:
                    stack2.append(char)
                elif brace == 2:
                    stack = [c + char for c in stack]
                    stack2 = []
                else:
                    stack.append(char)
                # print stack
                
        stack.sort() 
        stack.sort(key = len) 
        return stack

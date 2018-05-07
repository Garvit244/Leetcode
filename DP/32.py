class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [-1], 0

        for index in range(len(s)):
        	if s[index] == '(':
        		stack.append(index)
        	else:
        		currIndex = stack.pop()
        		if currIndex == -1:
        			stack.append(index)
        		else:
        			result = max(result, index-currIndex+1)
        return result
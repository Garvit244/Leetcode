class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif stack and parentheses[stack[-1]] == char:
                stack.pop()
            else:
                return False
        
        return not stack
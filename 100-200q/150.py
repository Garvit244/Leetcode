'''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, /. Each operand may be an integer or another expression.

    Note:

    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
    Example 1:

    Input: ["2", "1", "+", "3", "*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    Example 2:

    Input: ["4", "13", "5", "/", "+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        if not tokens:
            return 0
        
        stack = []
        for val in tokens:
            if val == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif val == '-':
                val1  = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
            elif val == '*':
                val1  = stack.pop()
                val2  = stack.pop()
                stack.append(val2*val1)
            elif val == '/':
                val1 = stack.pop()
                val2  = stack.pop()
                if val1*val2 < 0:
                    stack.append(-(-val2/val1))
                else:
                    stack.append(val2/val1)
            else:
                stack.append(int(val))
        return stack[0]
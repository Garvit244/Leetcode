'''
	Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	getMin() -- Retrieve the minimum element in the stack.
	Example:
	MinStack minStack = new MinStack();
	minStack.push(-2);
	minStack.push(0);
	minStack.push(-3);
	minStack.getMin();   --> Returns -3.
	minStack.pop();
	minStack.top();      --> Returns 0.
	minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  
        self.minimum = float('inf')      

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
        	self.stack.append(x)
        	self.minimum = x
        else:
        	if x < self.minimum:
        		self.stack.append(2*x-self.minimum)
        		self.minimum = x
        	else:
        		self.stack.append(x)

        print self.stack
                

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
        	top = self.stack.pop()
        	if top < self.minimum:
        		self.minimum = 2*self.minimum - top
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
        	return None
        else:
        	top = self.stack[-1]
        	if top < self.minimum:
        		return self.minimum
        	else:
        		return top
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
        	return self.minimum
        else:
        	return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
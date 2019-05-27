'''
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
'''
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        result = 0

        prefix_sum = [0]*(len(customers)+1)
        index = 0
        for customer, grump in zip(customers, grumpy):
            prefix_sum[index+1] = prefix_sum[index]
            if grump == 0:
                result += customer
            else:
                prefix_sum[index+1] += customer
            index += 1
        # print prefix_sum
        curr_max = result + prefix_sum[X]
        # print curr_max
        for index in range(X+1, len(prefix_sum)):
            temp_max = result + prefix_sum[index] - prefix_sum[index-X]
            # print temp_max
            curr_max = max(curr_max, temp_max)
        return curr_max

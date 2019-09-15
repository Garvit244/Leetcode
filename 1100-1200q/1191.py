'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
'''
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def kadane(arr):
            curr_sum, max_sum = arr[0], arr[0]
            for index in range(1, len(arr)):
                curr_sum = max(arr[index], curr_sum + arr[index])
                max_sum = max(max_sum, curr_sum)
            return max_sum

        def prefix(arr):
            curr_sum, max_val = 0, float('-inf')
            for index, val in enumerate(arr):
                curr_sum += val
                max_val = max(max_val, curr_sum)
            return max_val
        
        def suffix(arr):
            curr_sum, max_val = 0, float('-inf')
            for index in range(len(arr)-1, -1, -1):
                curr_sum += arr[index]
                max_val = max(max_val, curr_sum)
            return max_val
        
        if not arr:
            return 0
        if k == 1:
            return max(0, kadane(arr)) % (10 ** 9 + 7)
        else:
            return max(0, max((prefix(arr) + suffix(arr) + (k-2)*max(sum(arr), 0), kadane(arr)))) % (10 ** 9 + 7)

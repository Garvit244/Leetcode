'''
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
'''

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        forward = [0] * len(arr)
        backward = [0] * len(arr)
        
        curr_max, max_so_far = arr[0], arr[0]
        forward[0] = arr[0]
        for index in range(1, len(arr)):
            curr_max = max(arr[index], curr_max + arr[index])
            max_so_far = max(max_so_far, curr_max)
            
            forward[index] = curr_max
            
        curr_max = arr[len(arr) - 1]
        max_so_far = arr[len(arr) - 1]
        backward[len(arr) - 1] = arr[len(arr) - 1]
        
        index = len(arr) - 2
        while index >= 0:
            curr_max = max(arr[index], curr_max + arr[index])
            max_so_far = max(max_so_far, curr_max)
            
            backward[index] = curr_max
            index -= 1
            
        result = max_so_far
        for index in range(1, len(arr)-1):
            result = max(result, forward[index-1] + backward[index + 1])
        return result

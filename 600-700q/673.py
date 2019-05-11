'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''

class Solution(object):
    def findNumberOfLIS(self, nums):
        length = [1]*len(nums)
        count = [1]*len(nums)
        result = 0
        for end, num in enumerate(nums):
            for start in range(end):
                if num > nums[start]:
                    if length[start] >= length[end]:
                        length[end] = 1+length[start]
                        count[end] = count[start]
                    elif length[start] + 1 == length[end]:
                        count[end] += count[start]
        for index, max_subs in enumerate(count):
            if length[index] == max(length):
                result += max_subs
        return result

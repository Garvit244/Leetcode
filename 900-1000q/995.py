'''
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2]
'''

class Solution:
    def minKBitFlips(self, a: 'List[int]', k: 'int') -> 'int':
        from collections import deque
        q = deque()
        res = 0
        for i in range(len(a)):
            if len(q) % 2 != 0:
                if a[i] == 1:
                    res += 1
                    q.append(i+k-1)
            else:
                if a[i] == 0:
                    res += 1
                    q.append(i+k-1)
            if q and q[0] == i: q.popleft()
            if q and q[-1] >= len(a): return -1
        return res    
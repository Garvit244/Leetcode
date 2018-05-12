class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        
        A = [0] * (n + 1)
        count = 0
        
        for pointer1 in range(2, n):
            if A[pointer1] == 0:
                count += 1
                pointer2 = pointer1
                while (pointer2 + pointer1 < n):
                    pointer2 += pointer1
                    A[pointer2] = 1
                    
        return count
        
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashTable ={}
        
        for a in A:
            for b in B:
                if a+b in hashTable:
                    hashTable[a+b] += 1
                else:
                    hashTable[a+b] = 1
                    
        result = 0
        for c in C:
            for d in D:
                if -(c+d) in hashTable:
                    result += hashTable[-(c+d)]
        return result
        
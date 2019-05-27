'''
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        import heapq
        di = collections.Counter(barcodes)
        pq = [(-value, key) for key, value in di.items()]
        heapq.heapify(pq)
        # print pq
        result = []
        while len(pq) >= 2:
            freq1, barcode1 = heapq.heappop(pq)
            freq2, barcode2 = heapq.heappop(pq)
            result.extend([barcode1, barcode2])
            
            if freq1 + 1: 
                heapq.heappush(pq, (freq1 + 1, barcode1))
            if freq2 + 1: 
                heapq.heappush(pq, (freq2 + 1, barcode2))
                
        if pq:
            result.append(pq[0][1])
        
        return result

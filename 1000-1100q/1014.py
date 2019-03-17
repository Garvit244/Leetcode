'''
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

'''


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        high, low = sum(weights)+1, max(weights)
        
        while(low < high):
            mid = (high+low)/2
            temp_left = mid
            packet_at_left = D-1
            for weight in weights:
                if weight <= mid:
                    if temp_left < weight:
                        if packet_at_left == 0:
                            low = mid+1
                            break
                        packet_at_left -= 1
                        temp_left = mid-weight
                    else:
                        temp_left -= weight
            else:
                high = mid
                
        return low


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        
        while left < right:
            curr_sum, groups, invalid = 0, 0, True
            mid = left + ((right-left) >> 1)
            for weight in weights:
                if weight > mid:
                    invalid = False
                    break
                if curr_sum + weight > mid:
                    groups += 1
                    curr_sum = 0
                curr_sum += weight
            if invalid and groups < D:
                right = mid
            else:
                left = mid + 1
        return left
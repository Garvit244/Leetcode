'''
	There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

	You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

	Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, curr_sum, total_sum =0, 0, 0
        for index in range(len(gas)):
            diff = gas[index] - cost[index]
            total_sum += diff
            curr_sum += diff
            
            if curr_sum < 0:
                start = index + 1
                curr_sum = 0
                
        if total_sum >= 0:
            return start
        return -1
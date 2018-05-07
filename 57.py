'''
	Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

	You may assume that the intervals were initially sorted according to their start times.

	Example 1:

	Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
	Output: [[1,5],[6,9]]
	Example 2:

	Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
	Output: [[1,2],[3,10],[12,16]]
	Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
        	if newInterval.start > interval.end:
        		result.append(interval)
        	elif newInterval.end < interval.start:
        		result.append(newInterval)
        		newInterval = interval
        	elif newInterval.start <= interval.end or newInterval.end >= interval.start:
        		newInterval = Interval(min(newInterval.start, interval.start), max(interval.end, newInterval.end))

        result.append(newInterval)
       	return result
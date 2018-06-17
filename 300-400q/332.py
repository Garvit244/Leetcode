'''
	Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

	Note:

	If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
	All airports are represented by three capital letters (IATA code).
	You may assume all tickets form at least one valid itinerary.
	Example 1:

	Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
	Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        trips = defaultdict(list)
        for x in tickets:
            trips[x[0]].append(x[1])
        for x in trips:
            trips[x].sort()
        iter = ["JFK"]
        
        def dfs(curr_iter):
            if len(curr_iter) == n+1: 
                return curr_iter
            curr_stop = curr_iter[-1]
            
            if trips[curr_stop] == []: 
                return None
            
            next_stops = trips[curr_stop]
            i = 0
            for stop in next_stops:
                curr_iter.append(stop)
                del trips[curr_stop][i]
                
                if dfs(curr_iter): 
                    return curr_iter
                
                curr_iter.pop()
                trips[curr_stop].insert(i, stop)
                i += 1
            return None
        
        return dfs(iter)  
import heapq

class f(object):
	def __init__(self, x, h, s):
		self.x = x
		self.h = h
		self.s = s

	def __lt__(self, other):
		if self.x != other.x:
			return self.x < other.x
		else:
			if self.s and other.s:
				return self.h > other.h
			elif not self.s and not other.s:
				return self.h < other.h
			else:
				return self.s > other.s
            
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        
        building_list = []
        for x in range(len(buildings)):
            building_list.append(f(buildings[x][0], buildings[x][2], 1))
            building_list.append(f(buildings[x][1], buildings[x][2], 0))
            
        building_list = sorted(building_list)
        for buil in building_list:
            print buil.x, buil.h, buil.s
        heap = [0]
        result = []
        curr_max = heap[0]
        
        for building in building_list:
            heapq._heapify_max(heap)
            
            if building.s:
                heap.append(building.h)
                heapq._heapify_max(heap)
                new_max = heap[0]
                
                if curr_max != new_max:
                    result.append([building.x, building.h])
                    curr_max = new_max
            else:
                heap.remove(building.h)
                heapq._heapify_max(heap)
                new_max = heap[0]
                
                if new_max != curr_max:
                    result.append([building.x, new_max])
                    curr_max = new_max
                    
        return result
                
            
            
        
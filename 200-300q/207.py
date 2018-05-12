'''
	There are a total of n courses you have to take, labeled from 0 to n-1.

	Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

	Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

	Example 1:

	Input: 2, [[1,0]] 
	Output: true
	Explanation: There are a total of 2 courses to take. 
	             To take course 1 you should have finished course 0. So it is possible.

'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        stack = [False for _ in range(numCourses)]

        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        for course in range(numCourses):
        	if visited[course] == False:
        		if self.dfs(graph, visited, stack, course):
        			return False 
        return True

    def dfs(self, graph, visited, stack, course):
    	visited[course] = True
    	stack[course] = True

    	for neigh in graph[course]:
    		if visited[neigh] == False:
    			if self.dfs(graph, visited, stack, neigh):
    				return True

    		elif stack[neigh]:
    			return True
    	stack[course] = False
    	return False
        
'''
	There are a total of n courses you have to take, labeled from 0 to n-1.

	Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

	Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

	There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

	Example 1:

	Input: 2, [[1,0]] 
	Output: [0,1]
	Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
	             course 0. So the correct course order is [0,1] .
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        stack = [False for _ in range(numCourses)]

        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        result = []
        for course in range(numCourses):
        	if visited[course] == False:
        		if self.dfs(graph, visited, stack, course, result):
        			return []
        return result

    def dfs(self, graph, visited, stack, course, result):
    	visited[course] = True
    	stack[course] = True

    	for neigh in graph[course]:
    		if visited[neigh] == False:
    			if self.dfs(graph, visited, stack, neigh, result):
    				return True

    		elif stack[neigh]:
    			return True
    	stack[course] = False
    	result.append(course)
    	return False
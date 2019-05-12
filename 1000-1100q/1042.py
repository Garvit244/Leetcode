'''
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
'''

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """            
        plant = [1, 2, 3, 4]
        result = [0 for _ in range(N)]
        if not paths:
            return [plant[index%4] for index in range(N)]
        # print result
        change = {}
        update = []
        for path in paths:
            x, y = path[0]-1, path[1]-1
                
            if x in change:
                change[x].append(y)
            else:
                change[x] = [y]
                
            if y in change:
                change[y].append(x)
            else:
                change[y] = [x]
        
        for garden in range(N):
            color_used = []
            if garden in change:
                subgarden = change[garden]
                for subgarden in change[garden]:
                    if result[subgarden]:
                        color_used.append(result[subgarden])
            color_rem = list(set([1, 2, 3, 4]) - set(color_used))
            for color in color_rem:
                result[garden] = color
                break
        return result
 
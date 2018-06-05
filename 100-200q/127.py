'''
	Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

	Only one letter can be changed at a time.
	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
	Note:

	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.
	Example 1:

	Input:
	beginWord = "hit",
	endWord = "cog",
	wordList = ["hot","dot","dog","lot","log","cog"]

	Output: 5

	Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
	return its length 5.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        d = {}
        for word in wordList:
        	for i in range(len(word)):
        		s = word[:i] + "_" + word[i+1:]
        		if s in d:
        			d[s].append(word)
        		else:
        			d[s] = [word]
        print d
        queue, visited = [], set()
        queue.append((beginWord, 1))
        while queue:
        	word, steps = queue.pop(0)
        	if word not in visited:
        		visited.add(word)

        		if word == endWord:
        			return steps
        		else:
	        		for index in range(len(word)):
	        			s = word[:index] + "_" + word[index+1:]
	        			neigh_words = []
	        			if s in d:
	        				neigh_words = d[s]

	        			for neigh in neigh_words:
	        				if neigh not in visited:
	        					queue.append((neigh, steps+1))
        return 0

Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]  )
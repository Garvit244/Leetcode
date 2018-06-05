class TrieNode(object):
    def __init__(self):
        self.value, self.links = None, [None]*26

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        return

    def insert(self, word):
        if word:
            curr = self.root
            for ch in word:
                offset = ord(ch)-ord('a')
                if curr.links[offset] == None:
                    curr.links[offset] = TrieNode()
                curr = curr.links[offset]
            curr.value = word
        return
        
class Solution(object):
    def helper(self, x, y, board, trie_node, result):
        if trie_node.value:
            result.add(trie_node.value) # Look for other soln even if a soln is found. soln could a prefix of another soln.
        for x1,y1 in ((x+1,y), (x-1,y), (x, y+1), (x, y-1)):
            if 0<=x1<len(board) and 0<=y1<len(board[0]) and board[x1][y1] != -1 and trie_node.links[ord(board[x1][y1])-ord('a')]:
                ch, board[x1][y1] = board[x1][y1], -1
                self.helper(x1, y1, board, trie_node.links[ord(ch)-ord('a')], result)
                board[x1][y1] = ch
        return
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = set([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if trie.root.links[ord(board[i][j])-ord('a')]: 
                    ch, board[i][j] = board[i][j], -1
                    self.helper(i, j, board, trie.root.links[ord(ch)-ord('a')], result)
                    board[i][j] = ch
        return [x for x in result]    
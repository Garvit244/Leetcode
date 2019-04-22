'''
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
'''

class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.word = False
        
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie_node = Trie()
        for word in words:
            ptr = self.trie_node
            for char in reversed(word):
                if char not in ptr.nodes:
                    ptr.nodes[char] = Trie()
                ptr = ptr.nodes[char]
            ptr.word = True
        self.stream = []
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.append(letter)
        root = self.trie_node
        for char in reversed(self.stream):
            if char not in root.nodes:
                return False
            if root.nodes[char].word:
                return True
            root = root.nodes[char]
            
        return root.word
            
 

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
'''
	Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

	get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
	put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

	Follow up:
	Could you do both operations in O(1) time complexity?

	Example:

	LRUCache cache = new LRUCache( 2 /* capacity */ );

	cache.put(1, 1);
	cache.put(2, 2);
	cache.get(1);       // returns 1
	cache.put(3, 3);    // evicts key 2
	cache.get(2);       // returns -1 (not found)
	cache.put(4, 4);    // evicts key 1
	cache.get(1);       // returns -1 (not found)
	cache.get(3);       // returns 3
	cache.get(4);       // returns 4

'''

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mapping = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key in self.mapping:
            self.remove(self.mapping[key])
            
        node = Node(key, value)
        if len(self.mapping) >= self.capacity:
            next_head = self.head.next
            self.remove(next_head)
            del self.mapping[next_head.key]
            
        self.add(node)
        self.mapping[key] = node
        
    def add(self, node):
        tail = self.tail.prev
        tail.next = node
        self.tail.prev = node
        node.prev = tail
        node.next = self.tail
        
    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
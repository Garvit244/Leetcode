'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
'''

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        if not tiles:
            return 0
        
        import collections
        unique = set(tiles)
        freq_map =  collections.Counter(tiles)
        total_len = 1
        while total_len < len(tiles):
            new = set()
            for char in tiles:
                for comb in unique:
                    new_seq = comb+char
                    up_freq = collections.Counter(new_seq)
                    flag =True
                    for key, val in up_freq.items():
                        if val > freq_map[key]:
                            flag = False
                    if flag:
                        new.add(new_seq)
            # print new
            unique.update(new)
                    
            total_len += 1
        return len(unique)

'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        char_map = {}
        for char in A[0]:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
    
        int_map = {}
        for index in range(1, len(A)):
            for char in char_map.keys():
                if char in A[index]:
                    char_count = min(A[index].count(char), char_map[char])
                    char_map[char] = char_count
                else:
                    del char_map[char]
                    
        result = []
        for key, value in char_map.items():
            result.extend([key]*value)

        return result

'''
Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

 
Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"
 

Note:

1 <= text.length <= 1000
text consists of lowercase English letters.
'''
class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        if not text:
            return ''
        import collections
        freq_map = collections.Counter(text)
        used = [False]*26
        result = ''
        
        for char in text:
            freq_map[char] -= 1
            if used[ord(char)-97]:
                continue
            while (result and result[-1] > char and freq_map[result[-1]] > 0):
                used[ord(result[-1])-97] = False
                result = result[:-1]
                
            used[ord(char)-97] = True
            result += char
        return result

'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def lcs(A, B):
            n, m = len(A)+1, len(B)+1
            dp = [["" for _ in range(m)] for _ in range(n)]
            for index_i in range(1, n):
                for index_j in range(1, m):
                    if A[index_i-1] == B[index_j-1]:
                        dp[index_i][index_j] = dp[index_i-1][index_j-1] + A[index_i - 1]
                    else:
                        dp[index_i][index_j] = max(dp[index_i-1][index_j], dp[index_i][index_j-1], key=len)
            return dp[-1][-1]
        
        result = ""
        index_i, index_j = 0, 0
        for s in lcs(str1, str2):
            while str1[index_i] != s:
                result += str1[index_i]
                index_i += 1
            while str2[index_j] != s:
                result += str2[index_j]
                index_j += 1
                
            result += s
            index_i, index_j = index_i+1, index_j+1
            
        return result + str1[index_i:] + str2[index_j:]

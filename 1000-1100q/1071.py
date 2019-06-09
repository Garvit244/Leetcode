'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)  > len(str2):
            str1, str2 = str2, str1
            
        l_str1 = len(str1)
        for index in range(1, len(str1)+1):
            if l_str1%index != 0:
                continue
                
            size_to_take = int(l_str1/index)
            substr1 = str1[:size_to_take]
            substr2 = str2
            
            while substr1 == substr2[:size_to_take]:
                substr2 = substr2[size_to_take:]
                
            if substr2 == "":
                return substr1
        return ""

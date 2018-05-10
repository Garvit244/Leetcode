'''
    Given a string containing only digits, restore it by returning all possible valid IP address combinations.

    Example:

    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def dfs(s, temp, count):
            if count == 4:
                if not s:
                    result.append(temp[:-1])
                    return

            for index in range(1, 4):
                if index <= len(s):
                    if index == 1:
                        dfs(s[index:], temp + s[:index] + ".", count+1)
                    elif index ==2 and s[0] != '0':
                        dfs(s[index:], temp + s[:index] + ".", count+1)
                    elif index == 3 and s[0] != '0' and int(s[:3]) <= 255:
                        dfs(s[index:], temp + s[:index] + ".", count+1)

        dfs(s, "", 0)
        return result
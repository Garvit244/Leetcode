'''
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
'''

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        equal_list, unequal_list = [], []
        for equation in equations:
            x, y = equation[0], equation[3]
            if '==' in equation:
                if not equal_list:
                    equal_list.append(x+y)
                else:
                    found = False
                    for index in range(0, len(equal_list)):
                        val = equal_list[index]
                        if x in val or y in val:
                            val = val+x+y
                            equal_list[index] = val
                            found = True
                    if not found:
                        equal_list.append(x+y)
            else:
                if x == y:
                    return False
                unequal_list.append([x, y])
        
        for val in unequal_list:
            for equal in equal_list:
                if val[0] in equal and val[1] in equal:
                    return False
        return True

'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        start = int(str(low)[0])
        for val in range(1, len(str(low))):
            new_val = start%10 + 1
            start = start*10 + new_val
        if start > high:
            return result
        
        result.append(start)
        
        while result[-1] <= high:
            temp = str(result[-1])
            next_elem = int(temp[-1]) + 1

            if next_elem > 9:
                next_greater = 0
                for index in range(len(temp) + 1):
                    next_greater = next_greater*10 + (index+1)
            else:
                next_greater = int(temp[1:]) * 10 + next_elem
            if next_greater <= high:
                result.append(next_greater)
            else:
                break
            # print next_greater
        final_result = []
        for val in result:
            if '0' not in str(val) and val >= low:
                final_result.append(val)
        return final_result

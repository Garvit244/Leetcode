'''
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
        	return s

        result = ["" for _ in range(numRows)]
        row, down = 0, 1
        for char in s:
        	result[row] += char

        	if row == numRows - 1:
        		down = 0
        	if row == 0:
        		down = 1

        	if down:
        		row += 1
        	else:
        		row -= 1
        final_string = ""
        for value in result:
        	final_string += value
        return final_string

print Solution().convert("PAYPALISHIRING",3)


'''
Alternative Solution
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        out = [[] for _ in range(numRows)]
        goingDown = False
        nextt = 0
        for char in s:
            out[nextt].append(char)
            if nextt == 0 or nextt == numRows - 1:
                goingDown = not goingDown
            if not goingDown: nextt += 1
            else: nextt -= 1
        return ''.join(["".join(arr) for arr in out])

class Solution:
    def romanToInt(self, s: str) -> int:
        letter = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = 0
        
        while s:
            if s[0:2] in letter:
                result += letter.get(s[0:2])
                s = s[2:]
            else:
                result += letter.get(s[0])
                s = s[1:]
        
        return result
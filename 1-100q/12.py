# 1 -> "I"
# 2 -> "II"
# 3 -> "III"
# 4 -> "IV"
# 5 -> "V"
# 1499 -> "MCDXCIX"


class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ""
        i = 0
        
        while num > 0:
            times = num // nums[i]
            
            result += letters[i] * times
            num -= nums[i] * times
            
            i += 1
        
        return result
        
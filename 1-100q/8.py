class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        number = ""
        
        
        for x in str:
            if x.isalpha() and number == "":
                return 0
            elif x.isalpha():
                break
            elif x == ".":
                break
            elif x == " ":
                break
            elif (x == "+" or x == "-") and number == "":
                number = number + x
            elif (x == "+" or x == "-") and number != "":
                break
            elif (x == "+" or x == "-") and (number[-1] == "+" or number[-1] == "-"):
                return 0
            elif (x == "+" or x == "-") and ("+" in number or "-" in number):
                break
            elif x.isdigit():
                number = number + x
        if number == "" or number == "+" or number == "-":
            return 0
        else:
            if int(number) > ((2**31)-1):
                return (2**31)-1
            elif int(number) < -(2**31):
                return -(2**31)
            else:
                return int(number)
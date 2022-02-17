class Solution:
    def reverse(self, x: int) -> int:
        revx = int(str(x)[::-1].replace("-", ""))
        
        if x < 0:
            revx *= -1
            
        if revx >= 2**31-1 or revx <= -2**31:
            return 0
        
        return revx
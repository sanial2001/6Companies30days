class Solution:
    def titleToNumber(self, col: str) -> int:
        num = ord(col[0])-64
        for i in range(1, len(col)):
            num = 26*num + (ord(col[i])-64)
        return num
            

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while(b):
            a,b=a^b,(a&b)<<1
        return a
        
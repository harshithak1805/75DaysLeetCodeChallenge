class Solution:
    def addDigits(self, n: int) -> int:
        while n>=10:
            t=0
            while n>0:
                t+=n%10
                n//=10
            n=t
        return n



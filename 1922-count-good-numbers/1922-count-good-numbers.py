class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m=10**9 +7
        e=(n+1)//2
        o=n//2
        return pow(5,e,m)*pow(4,o,m)%m
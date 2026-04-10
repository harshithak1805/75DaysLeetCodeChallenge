class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:].zfill(32)
        res=b[::-1]
        return int(res,2)
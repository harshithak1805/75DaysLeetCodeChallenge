class Solution:
    def canAliceWin(self, n: int) -> bool:
        c=False
        idx=10
        while True:
            if n-idx>=0:
                n=n-idx
                c=True if c==False else False
                idx=idx-1
            else:
                return c

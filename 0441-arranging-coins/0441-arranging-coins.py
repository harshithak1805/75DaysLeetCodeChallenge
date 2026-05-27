class Solution:
    def arrangeCoins(self, n: int) -> int:
        idx=1
        c=0
        while idx<=n:
            n=n-idx
            c+=1
            idx+=1
        return c
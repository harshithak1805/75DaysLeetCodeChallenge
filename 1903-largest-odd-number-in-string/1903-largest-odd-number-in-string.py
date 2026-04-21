class Solution:
    def largestOddNumber(self, n: str) -> str:
        for i in range(len(n)-1,-1,-1):
            if int(n[i])%2!=0:
                return n[:i+1]
        return ""
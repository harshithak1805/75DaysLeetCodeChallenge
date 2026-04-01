class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        s=s.strip()
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i]==" ":
                break
            else:
                l+=1
        return l

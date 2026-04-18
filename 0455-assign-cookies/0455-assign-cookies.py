class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=r=0
        n=len(g)
        m=len(s)
        g=sorted(g)
        s=sorted(s)
        
        while l<m and r<n:
            if g[r]<=s[l]:
                r+=1
            l+=1
        return r
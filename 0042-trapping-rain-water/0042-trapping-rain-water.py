class Solution:
    def trap(self, h: List[int]) -> int:
        n=len(h)
        l=0
        r=n-1
        res=0
        lm=rm=0
        while(l<r):
            lm=max(lm,h[l])
            rm=max(rm,h[r])
            if lm<rm:
                res+=lm-h[l]
                l+=1
            else:
                res+=rm-h[r]
                r-=1
        return res
class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        l=0
        r=n-1
        res=[]
        maxi=0
        while l<r:
            w=r-l
            ch=min(h[l],h[r])
            maxi=max(maxi,ch*w)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return maxi

    

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        x=set(s)
        lo={}
        for i in range(len(s)-1,-1,-1):
            if s[i] in lo:
                pass
            else:
                lo[s[i]]=i
        res=[]
        start=0
        while start<len(s):
            i=start
            end=lo[s[start]]
            while i<=end:
                if lo[s[i]]>end:
                    end=lo[s[i]]
                i+=1
            res.append(i-start)
            start=i
        return res
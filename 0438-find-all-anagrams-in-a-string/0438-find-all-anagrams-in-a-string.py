from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        else:
            res=[]
            w={}
            t={}
            for i in p:
                t[i]=t.get(i,0)+1
            for j in range(len(p)):
                w[s[j]]=w.get(s[j],0)+1
            if w==t:
                res.append(0)
            for j in range(1,len(s)-len(p)+1):
                w[s[j-1]]=w.get(s[j-1],0)-1
                if w[s[j-1]]==0:
                    del (w[s[j-1]])
                w[s[j+len(p)-1]]=w.get(s[j+len(p)-1],0)+1
                if w==t:
                    res.append(j)
            return res
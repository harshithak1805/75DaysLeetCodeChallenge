from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        frq=Counter(s)
        x=sorted(frq,key=lambda x:frq[x],reverse=True)
        res=""
        for i in x:
            res+=i*frq[i]
        return res
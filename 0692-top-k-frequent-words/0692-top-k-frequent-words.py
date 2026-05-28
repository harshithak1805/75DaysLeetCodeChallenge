from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h=Counter(words)
        res=[]
        idx=0
        h=sorted(h.items(),key=lambda x:(-x[1],x[0]))
        for i in range(k):
                res.append(h[i][0])
                idx+=1
        return res

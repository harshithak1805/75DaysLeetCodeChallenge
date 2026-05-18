import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=[]
        for i in stones:
            s.append(-i)
        heapq.heapify(s)
        while len(s)>1:
                n=len(s)
                p=-(heapq.heappop(s))
                q=-(heapq.heappop(s))
                x=(q-p)
                if p!=q:
                    heapq.heappush(s,x)
        if len(s)==1:
            return -1*s[0]
        else:
            return 0
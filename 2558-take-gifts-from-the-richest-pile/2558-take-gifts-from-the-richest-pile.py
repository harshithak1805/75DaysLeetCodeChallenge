import heapq,math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s=[]
        for i in gifts:
            s.append(-i)
        heapq.heapify(s)      
        for _ in range(k):
            x=int(math.sqrt(-heapq.heappop(s)))
            heapq.heappush(s,-x)
        return -(sum(s))

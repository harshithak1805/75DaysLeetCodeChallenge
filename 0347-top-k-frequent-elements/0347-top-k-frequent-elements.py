import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        h=[]
        r=[]
        for i,c in freq.items():
            heapq.heappush(h,(c,i))
            if len(h)>k: 
                (heapq.heappop(h))
        while h:
            c,i=heapq.heappop(h)
            r.append(i)
        return r
    
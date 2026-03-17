from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap=[]
        for x ,c in freq.items():
            heapq.heappush(heap,(c,x))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x for c,x in heap]
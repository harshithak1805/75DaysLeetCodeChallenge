import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        h=[]
        res=[]
        for i in nums:
            heapq.heappush(h,i)
        for i in range(len(nums)//2):
            x=heapq.heappop(h)
            y=heapq.heappop(h)
            res.append(y)
            res.append(x)
        return res

        

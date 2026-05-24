class Solution:
    def largestInteger(self, num: int) -> int:
        e=[]
        o=[]
        res=[]
        for i in str(num):
            if int(i)%2==0:
                heapq.heappush(e,-int(i))
            else:
                heapq.heappush(o,-int(i))
        for i in str(num):
            if int(i)%2==0:
                res.append(str(-heapq.heappop(e)))
            else:
                res.append(str(-heapq.heappop(o)))
        return int("".join(res))
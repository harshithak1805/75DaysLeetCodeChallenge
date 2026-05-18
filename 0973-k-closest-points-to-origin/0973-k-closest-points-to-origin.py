class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        res=[]
        x=0
        for i in points:
            d[x]=(i[0]**2 + i[1]**2)
            x+=1
        d=(sorted(d.items(),key=lambda x:x[1]))
        for i in range(k):
            res.append(points[d[i][0]])
        return res

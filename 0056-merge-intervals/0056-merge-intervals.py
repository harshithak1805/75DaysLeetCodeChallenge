class Solution:
    def merge(self, x: List[List[int]]) -> List[List[int]]:
        x=sorted(x,key=lambda y:y[0])
        res=[]
        res.append(x[0])
        for i in range(1,len(x)):
            if res[-1][1]>=x[i][0]:
                res[-1][1]=max(res[-1][1],x[i][1])
            else:
                res.append(x[i])
        return res
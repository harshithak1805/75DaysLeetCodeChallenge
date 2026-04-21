class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        it=sorted(intervals, key=lambda x:x[1])
        res=[]
        c=0
        res.append(it[0])
        for i in range(1,len(it)):
            if res[-1][1] > it[i][0]:
                c+=1
            else:
                res.append(it[i])
        return c

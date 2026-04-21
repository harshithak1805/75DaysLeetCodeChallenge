class Solution:
    def maximumUnits(self, boxtypes: List[List[int]], ts: int) -> int:
        bt=sorted(boxtypes,key=lambda x:x[1],reverse=True)
        size=0
        val=0
        for i in range(len(bt)):
            if size<ts:
                x=ts-size
                take=min(x,bt[i][0])
                val+=take*bt[i][1]
                size+=take
            else:
                    break
        return val


class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ind=(need1*cost1 + need2*cost2) 
        tog= max(need1,need2)*costBoth
        sep=min(need1,need2)*costBoth
        a=max(need1,need2)
        b=min(need1,need2)
        c=(a-b)
        calc=c*cost1 if need1>need2 else c*cost2
        res=sep+calc
        return min(tog,ind,res)
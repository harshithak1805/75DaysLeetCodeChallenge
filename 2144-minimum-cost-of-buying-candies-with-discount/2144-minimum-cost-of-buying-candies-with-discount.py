class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost,reverse=True)
        price=0  
        for i in range(len(cost)):
            if i%3!=2:
                price+=cost[i]
        return price
        
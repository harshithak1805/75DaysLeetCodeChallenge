class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    s.append(prices[i]-prices[j])
                    break
            else:
                s.append(prices[i])
        return s
                
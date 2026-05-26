class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        x=0
        while x<=k:
            if i not in arr:
                x+=1
                if x==k:
                    return i
            i+=1
        
            

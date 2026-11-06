class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        for i in arr1:
            res=[]
            for j in arr2:
                if abs(i-j)<=d:
                    res.append(j)
            if not res:
                c+=1
        return c
    
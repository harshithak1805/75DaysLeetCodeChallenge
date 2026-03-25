class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        a=set(a)
        b=set(b)
        res=[]
        for i in a:
            if i in b:
                if i not in res:
                    res.append(i)
        return res
                

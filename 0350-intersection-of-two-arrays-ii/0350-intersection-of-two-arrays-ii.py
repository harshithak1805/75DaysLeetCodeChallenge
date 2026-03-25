class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        i=0
        j=0
        a.sort()
        b.sort()
        res=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                res.append(a[i])
                i+=1
                j+=1
            elif a[i]>b[j]:
                j+=1
            else:
                i+=1
        return res
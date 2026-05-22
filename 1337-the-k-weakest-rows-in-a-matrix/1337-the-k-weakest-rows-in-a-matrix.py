class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r=[]
        for i in range(len(mat)):
            r.append((mat[i].count(1),i))
        r=sorted(r,key=lambda x:x[0])
        res=[]
        for i in range(k):
            res.append(r[i][1])
        return res
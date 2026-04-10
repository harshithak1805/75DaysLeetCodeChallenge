class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        rb=cb=0
        res=[]
        re=len(mat)-1
        ce=len(mat[0])-1
        while (rb<=re and cb<=ce):
            for i in range(cb,ce+1):
                res.append(mat[rb][i])
            rb+=1
            for i in range(rb,re+1):
                res.append(mat[i][ce])
            ce-=1
            if rb<=re:
                for i in range(ce,cb-1,-1):
                    res.append(mat[re][i])
            re-=1
            if cb<=ce:
                for i in range(re,rb-1,-1):
                    res.append(mat[i][cb])
            cb+=1
        return res
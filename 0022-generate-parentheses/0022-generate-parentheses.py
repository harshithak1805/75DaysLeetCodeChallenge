class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(curr,o,c,n,res):
            if len(curr)==2*n:
                res.append(curr)
                return 
            if o<n:
                bt(curr+"(",o+1,c,n,res)
            if o>c:
                bt(curr+")",o,c+1,n,res)
        def par(n):
            res=[]
            bt("",0,0,n,res)
            return res
        ans=[]
        ans=par(n)
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def bt(curr,o,c,n,res):
            if len(curr)==2*n:
                res.add(curr)
            if o<=n:
                bt(curr+"(",o+1,c,n,res)
            if c<=n:
                bt(curr+")",o,c+1,n,res)
        def valid(curr):
            stk=[]
            for i in curr:
                if i=="(":
                    stk.append(i)
                else:
                    if stk:
                        if stk[-1]=="(":
                            stk.pop()
                        else:
                            return False
                    else:
                        return False
            if stk:
                return False
            else:
                return True
        res=set()
        bt("",0,0,n,res)
        ans=[]
        for i in res:
            if valid(i):
                print(i)
                ans.append(i)
        return ans
                
                    
                

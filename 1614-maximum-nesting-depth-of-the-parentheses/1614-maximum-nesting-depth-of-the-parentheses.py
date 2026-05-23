class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        c=0
        stk=[]
        for i in s:
            if i=="(":
                c+=1
                maxi=max(c,maxi)
            elif i==")":
                c-=1
            else:
                pass
        return maxi

                

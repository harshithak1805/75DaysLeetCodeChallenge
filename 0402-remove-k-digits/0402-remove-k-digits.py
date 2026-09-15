class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return "0"
        else:
            stk=[]
            idx=0
            for i in num:
                while stk  and k>0 and stk[-1]>i:
                    stk.pop()
                    k-=1
                stk.append(i)
            while k>0:
                stk.pop()
                k-=1
            ans= "".join(stk).lstrip('0') 
            return ans if ans else "0"
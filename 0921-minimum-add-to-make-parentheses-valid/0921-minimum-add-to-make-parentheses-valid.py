class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk=[]
        for i in s:
            if stk:
                if stk[-1]=="(" and i==")":
                    stk.pop()
                else:
                    stk.append(i)
            else:
                stk.append(i)   
        return len(stk)
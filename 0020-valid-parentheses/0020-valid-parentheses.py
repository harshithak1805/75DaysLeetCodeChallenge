
class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        n=len(s)
        for i in range(n):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stk.append(s[i])
            else:
                if len(stk)==0:
                    return False
                if (stk[-1]=="(" and s[i]==")") or (stk[-1]=="[" and s[i]=="]") or (stk[-1]=="{" and s[i]=="}"):
                    stk.pop()
                else:
                    return False
        return len(stk)==0
        
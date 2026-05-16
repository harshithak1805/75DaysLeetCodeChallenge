class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i in "([{":
                stk.append(i)
            else:
                if not stk:
                    return False
                if (stk[-1] == "(" and i == ")") or \
                (stk[-1]=="{" and i=="}") or \
                (stk[-1]=="[" and i=="]"):
                    stk.pop()
                else:
                    return False
        return len(stk)==0
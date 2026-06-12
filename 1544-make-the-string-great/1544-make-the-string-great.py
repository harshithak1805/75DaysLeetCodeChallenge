class Solution:
    def makeGood(self, s: str) -> str:
        stk=[]
        for ch in s:
            if stk and abs(ord(stk[-1])-ord(ch))==32:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)
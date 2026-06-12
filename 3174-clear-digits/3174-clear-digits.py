class Solution:
    def clearDigits(self, s: str) -> str:
        stk=[]
        for i in s:
            if not i.isdigit():
                stk.append(i)
            else:
                stk.pop()
        return "".join(stk)
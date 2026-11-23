class Solution:
    def checkString(self, s: str) -> bool:
        stk=[]
        for i in s:
            if stk:
                if i=="a":
                    if stk[-1]!="b":
                        stk.append(i)
                    else:
                        return False
            stk.append(i)
        return True
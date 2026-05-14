class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i=="#":
                if not len(a)<1:
                    a.pop()
            else:
                a.append(i)
        for i in t:
            if i=="#":
                if not len(b)<1:
                    b.pop()
            else:
                b.append(i)
        if a==b:
            return True
        else:
            return False
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={}
        for i,ch in enumerate(s):
            last[ch]=i
        stk=[]
        seen=set()
        for i ,ch in enumerate(s):
            if ch in seen:
                continue
            while stk and stk[-1]>ch and last[stk[-1]]>i :
                seen.remove(stk.pop())
            seen.add(ch)
            stk.append(ch)
        return "".join(stk)
            
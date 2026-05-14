class Solution:
    def removeDuplicates(self, s: str) -> str:
        r=[]
        for i in range(len(s)):
            if len(r)>0 and r[-1]==s[i]:
                r.pop()
            else:
                r.append(s[i])
        return "".join(r)

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        c2=0
        i2=0
        c1=0
        seen={}
        if set(s2)-set(s1):
            return 0
        while c1<n1:
            for ch in s1:
                if ch==s2[i2]:
                    i2+=1
                if i2==len(s2):
                    c2+=1
                    i2=0
            c1+=1
            if i2 in seen:
                p1,p2=seen[i2]
                cycle_s1=c1-p1
                cycle_s2=c2-p2
                r=n1-c1
                times=r//cycle_s1
                c2+=times*cycle_s2
                c1+=times*cycle_s1
            else:
                seen[i2]=(c1,c2)
        return c2//n2
class Solution:
    def reverseByType(self, s: str) -> str:
        sc=[]
        a=[]
        for i in s:
            if i.isalpha():
                a.append(i)
            else:
                sc.append(i)
        a=a[::-1]
        i=0
        j=0
        k=0
        sc=sc[::-1]
        res=[]
        for z in s:
                if z.isalpha():
                    res.append(a[i])
                    i+=1
                else:
                    res.append(sc[j])
                    j+=1
        return "".join(res)


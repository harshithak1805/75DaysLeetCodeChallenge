class Solution:
    def divide(self, dd: int, dr: int) -> int:
        if dd==dr:
            return 1
        sign=True
        if (dd>=0 and dr<0) or (dd<0 and dr>0):
            sign=False 
        n=abs(dd)
        d=abs(dr)
        ans=0
        while n>=d:
            c=0
            while n>=(d<<(c+1)):
                c+=1
            ans+=2**c
            n-=d<<c
        if ans >=2**31 and sign==True:
            return 2**31-1
        if ans>=2**31 and sign==False:
            return -2**31
        if sign==True:
            return ans
        else:
            return -ans

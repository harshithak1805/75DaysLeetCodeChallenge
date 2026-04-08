class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                if not f:
                    return False
                else:
                    f-=1
                    t+=1
            else:
                if t and f:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True
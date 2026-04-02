class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0]*n
        stk=[]
        for i in range(n):
            while stk and temp[i]>temp[stk[-1]]:
                index=stk.pop()
                res[index]=i-index
            stk.append(i)
        return res

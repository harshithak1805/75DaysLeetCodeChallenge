class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        res=[]
        for i in nums:
            if c[i] == 1:
                res.append(i)
        return res
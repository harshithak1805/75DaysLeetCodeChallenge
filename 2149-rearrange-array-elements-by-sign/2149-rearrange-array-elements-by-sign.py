class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        i=0
        j=0
        res=[]
        while i<len(p) and j<len(n):
            res.append(p[i])
            i+=1
            res.append(n[j])
            j+=1
        return res
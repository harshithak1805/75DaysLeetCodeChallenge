class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for m in range(2**n):
            sub=[]
            for i in range(n):
                if m&(1<<i):
                    sub.append(nums[i])
            res.append(sub)
        return res
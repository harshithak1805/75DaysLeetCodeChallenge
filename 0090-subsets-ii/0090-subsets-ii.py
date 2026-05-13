class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for m in range(2**n):
            s=[]
            for i in range(n):
                if m&(1<<i):
                    s.append(nums[i])
            if s not in res:
                res.append(s)
        return res
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc=0
        pc=0
        n=len(nums)
        for i in range(n):
            if nums[i]<0:
                nc+=1
            elif nums[i]>0:
                pc+=1
        return max(pc,nc)
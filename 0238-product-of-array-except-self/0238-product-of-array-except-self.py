class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=1
        suf=1
        ans=[1]*n
        for i in range(n):
            ans[i]=pre
            pre*=nums[i]
        for i in range(n-1,-1,-1):
            ans[i]*=suf
            suf*=nums[i]
        return ans



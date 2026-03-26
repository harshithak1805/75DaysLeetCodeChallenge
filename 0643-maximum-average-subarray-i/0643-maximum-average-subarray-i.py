class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum=0
        for i in range(k):
            wsum=wsum+nums[i]
        msum=wsum
        for j in range(k,len(nums)):
            wsum=wsum-nums[j-k]+nums[j]
            msum=max(msum,wsum)
        return msum/k
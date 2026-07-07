class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        best=float("-inf")
        for i in nums:
            sums+=i
            best=max(best,sums)
            if sums<0:
                sums=0
        return best
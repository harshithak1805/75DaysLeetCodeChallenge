class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        sums=0
        for i in range(0,len(nums),2):
            sums+=min(nums[i],nums[i+1])
        return sums
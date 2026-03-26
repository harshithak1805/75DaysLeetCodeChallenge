class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        for i in range(len(nums)):
            r=sum(nums)-l-nums[i]
            if l==r:
                return i
            l+=nums[i]
        return -1
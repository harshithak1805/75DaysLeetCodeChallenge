class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi_val=max(nums)
        maxi_index=nums.index(maxi_val)
        for i in range(len(nums)):
            if i!=maxi_index:
                if maxi_val<2*nums[i]:
                    return -1
        return maxi_index

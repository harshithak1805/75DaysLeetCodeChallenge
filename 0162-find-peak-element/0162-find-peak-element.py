class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)>2:
            for i in range(1,len(nums)):
                if i==0:
                    if nums[i]>nums[i+1]:
                        return i
                elif i==len(nums)-1:
                    if nums[i]>nums[i-1]:
                        return i
                elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    return i
        elif len(nums)==1:
            return 0
        else:
            if nums[0]>nums[1]:
                return 0
            elif nums[1]>nums[0]:
                return 1
        return 0
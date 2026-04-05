class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=0
        if 0 not in nums:
            for i in range(len(nums)):
                if nums[i]<0:
                    c+=1
            if c%2==0:
                return 1
            else:
                return -1
        else:
            return 0
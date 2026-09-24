class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            sums=0
            s=str(nums[i])
            for j in range(len(s)):
                sums+=int(s[j])
            if i==sums:
                return i
        else:
            return -1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        T=[1]*len(nums)
        max_index=0
        n=len(nums)
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                        T[i]=max(T[i],T[j]+1)
        
        for i in range(n):
            if T[i]>T[max_index]:
                max_index=i
        return max(T)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        i=0
        for j in nums:
            if j!=0:
                nums[i]=j
                i+=1
        for x in range(i,n):
            nums[x]=0
        return nums 

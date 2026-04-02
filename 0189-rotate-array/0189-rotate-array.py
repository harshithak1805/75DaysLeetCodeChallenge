class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        temp=nums[:n-k]
        for i in range(k):
            nums[i]=nums[n-k+i]
        for i in range(len(nums)-k):
            nums[k+i]=temp[i]
            
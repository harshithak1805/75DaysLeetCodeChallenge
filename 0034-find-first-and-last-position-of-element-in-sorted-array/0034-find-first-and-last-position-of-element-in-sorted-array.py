class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            if target not in nums:
                ans=-1
            else:
                n=len(nums)
                i=0
                ans=0
                j=n-1
                while i<=j : 
                    m=(i+j)//2
                    if nums[m]<target:
                        i=m+1
                    elif nums[m]>target:
                        j=m-1
                    else:
                        ans=m
                        j=m-1
            return ans
        def last(nums,target):
            n=len(nums)
            if target not in nums:
                ans=-1
            else:
                i=0
                ans=0
                j=n-1
                while i<=j : 
                    m=(i+j)//2
                    if nums[m]<target:
                        i=m+1
                    elif nums[m]>target:
                        j=m-1
                    else:
                        ans=m
                        i=m+1
            return ans

        return [first(nums,target),last(nums,target)]

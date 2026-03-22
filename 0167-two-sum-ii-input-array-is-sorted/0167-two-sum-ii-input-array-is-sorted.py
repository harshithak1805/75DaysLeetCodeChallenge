class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            l=0
            r=len(nums)-1
            while l<r:
                c=nums[l]+nums[r]
                if c==target:
                    return l+1,r+1
                elif c<target:
                    l+=1
                else:
                    r-=1

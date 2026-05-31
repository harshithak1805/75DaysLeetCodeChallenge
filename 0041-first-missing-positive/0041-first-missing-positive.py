class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        mini=min(nums)
        maxi=max(nums)
        n=len(nums)
        res=[]
        for i in range(n):
            if nums[i]<=0 :
                pass
            elif nums[i]>n:
                pass
            else:
                res.append(nums[i])
        res=sorted(set(res))
        x=1
        for i in range(len(res)):
            if res[i]==x:
                x+=1
            else:
                return x
        return x
        
        
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c=0
        res=1
        for i in range(len(nums)):
            sub=[]
            for j in range(i,len(nums)):
                if sub :
                    if sub[-1]<nums[j]:
                        sub.append(nums[j])
                        res=max(res,len(sub[:]))
                    else:
                        break
                else:
                    sub.append(nums[j])
        for i in range(len(nums)):
            sub=[]
            for j in range(i,len(nums)):
                if sub :
                    if sub[-1]>nums[j]:
                        sub.append(nums[j])    
                        res=max(res,len(sub[:]))
                    else:
                        break
                else:
                    sub.append(nums[j])
                    
        return res
                

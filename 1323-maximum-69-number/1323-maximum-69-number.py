class Solution:
    def maximum69Number (self, nums: int) -> int:
        nums=str(nums)
        c=0
        res=[]
        for i in range(len(nums)):
            if nums[i]=="6":
                if c==0:
                    res.append("9")
                    c+=1
                else:
                    res.append(nums[i])
            else:
                res.append(nums[i])
        r=int("".join(res))
        return r

            